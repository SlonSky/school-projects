import os
from datetime import datetime
from itertools import combinations, product
from pprint import pprint
import pandas as pd
import lightgbm as lgbm
import numpy as np
import joblib
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler

from db import Boxer, Referee, Place


class MLEngine:

    clf = None
    scaler = None
    clf_name = None

    def load_clf(self, filepath):
        self.clf = lgbm.Booster(model_file=filepath)
        self.clf_name = filepath.split(os.path.sep)[-2]

    def load_scaler(self, filepath):
        self.scaler = joblib.load(filepath)

    def prepare_data(self, boxers, referees, places, dates):
        opponents = list(combinations(boxers, 2))
        circs = list(product(opponents, referees, places, dates))

        data = []
        for i in circs:
            boxer_a = i[0][0]
            boxer_b = i[0][1]
            referee = i[1]
            place = i[2]
            date = i[3]
            date_month = datetime.strptime(date, '%d.%M.%Y').month
            data.append({
                'boxer_a_name': boxer_a.name,
                'boxer_b_name': boxer_b.name,
                'referee_name': referee.name,
                'place_name': place.name,
                'date': date,

                'boxer_a_won': boxer_a.won,
                'boxer_a_lost': boxer_a.lost,
                'boxer_a_drawn': boxer_a.drawn,
                'boxer_a_kos': boxer_a.kos,
                'boxer_a_experience': boxer_a.experience,
                'boxer_a_from_referee_country': boxer_a.country == referee.country,
                'boxer_a_bout_at_home': boxer_a.country == place.country,

                'boxer_b_won': boxer_b.won,
                'boxer_b_lost': boxer_b.lost,
                'boxer_b_drawn': boxer_b.drawn,
                'boxer_b_kos': boxer_b.kos,
                'boxer_b_experience': boxer_b.experience,
                'boxer_b_from_referee_country': boxer_b.country == referee.country,
                'boxer_b_bout_at_home': boxer_b.country == place.country,

                'boxers_from_same_country': boxer_a == boxer_b,

                'bout_season_autumn': 8 < date_month < 12,
                'bout_season_spring': 2 < date_month < 6,
                'bout_season_summer': 5 < date_month < 9,
                'bout_season_winter': date_month == 12 or 0 < date_month < 3
            })

        df = pd.DataFrame(data, columns=data[0].keys())

        return df

    def normalize_work_data(self, df):
        info = df.iloc[:, :5]
        X = df.iloc[:, 5:]

        X.loc[:, X.columns] = self.scaler.transform(X.loc[:, X.columns])
        return X, info

    def predict_work_data(self, X):
        Y = self.clf.predict(X)
        return Y

    def calc_uncert(self, Y):
        won_a = Y.copy()
        won_b = abs(Y.copy() - 1)

        uncertanity = self.gauss(won_a, won_b)

        return uncertanity

    def prepare_result(self, info, uncertanity):
        result = info.copy()
        result['Uncert'] = np.round(uncertanity, 3)

        return list(result.sort_values(by='Uncert', ascending=False).T.to_dict().values())

    def gauss(self, x1, x2):
        mu = 0.5
        sigma = 0.5 / 2
        return np.exp(-((x1 - 0.5) ** 2 / (2 * sigma ** 2) + (x2 - 0.5) ** 2 / (2 * sigma ** 2)))


    def read_train_data(self, filepath):

        df = pd.read_csv(filepath).drop(['Unnamed: 0'], axis=1)
        df = df[[
            'result',
            'boxer_a_won',
            'boxer_a_lost',
            'boxer_a_drawn',
            'boxer_a_kos',
            'boxer_b_won',
            'boxer_b_lost',
            'boxer_b_drawn',
            'boxer_b_kos',
            'boxers_from_same_country',
            'boxer_a_from_referee_country',
            'boxer_b_from_referee_country',
            'boxer_a_bout_at_home',
            'boxer_b_bout_at_home',
            'boxer_a_experience',
            'boxer_b_experience',
            'bout_season_autumn',
            'bout_season_spring',
            'bout_season_summer',
            'bout_season_winter']]

        return df

    def split_train_test(self, df):
        split_index = df.shape[0] * 0.8
        test_df = df.loc[split_index:]
        df = df.loc[:split_index]
        return df, test_df

    def categorize_data(self, df, test_df):
        DRAWN = 'drawn'

        df.drop(df[df.result == DRAWN].index, axis=0, inplace=True)
        test_df.drop(test_df[test_df.result == DRAWN].index, axis=0, inplace=True)

        WON_A = 'won_A'
        WON_B = 'won_B'
        RESULT_CATEGORIES = {
            WON_A: 0,
            WON_B: 1,
        }

        for k, v in RESULT_CATEGORIES.items():
            df.loc[df.result == k, 'result'] = v

        for k, v in RESULT_CATEGORIES.items():
            test_df.loc[test_df.result == k, 'result'] = v

        return df, test_df

    def normalize_data(self, df, test_df):
        input_cols = [i for i in df.columns if i != 'result']
        normed = df.copy()
        normed_test = test_df.copy()

        scaler = MinMaxScaler()
        normed.loc[:, input_cols] = scaler.fit_transform(normed.loc[:, input_cols])
        normed_test.loc[:, input_cols] = scaler.transform(normed_test.loc[:, input_cols])

        X_train = normed.loc[:, input_cols]
        Y_train = normed.result

        X_test = normed_test.loc[:, input_cols]
        Y_test = normed_test.result

        return scaler, X_train, Y_train, X_test, Y_test

    def train_clf(self, X_train, Y_train, X_test, Y_test, callback):
        d_train = lgbm.Dataset(X_train, Y_train)
        d_test = lgbm.Dataset(X_test, Y_test)

        params = {
            'objective': 'binary',
            'learning_rate': 0.01,
            'num_leaves': 700,
            'feature_fraction': 0.64,
            'bagging_fraction': 0.8,
            'bagging_freq': 1,
            'boosting_type': 'gbdt',
            'metric': 'binary_logloss'
        }

        bst = lgbm.train(params, d_train, 5000, valid_sets=[d_test], verbose_eval=50, early_stopping_rounds=100,
                         callbacks=[callback])

        return bst

    def estimate_clf(self, bst, X_test, Y_test):
        y_pred = bst.predict(X_test)
        y_pred[y_pred >= 0.5] = 1
        y_pred[y_pred <= 0.5] = 0
        return classification_report(Y_test, y_pred)

    def save_clf(self, bst, scaler, loc):

        ts = int(datetime.now().timestamp())
        dest = os.path.join(loc, str(ts))
        if not os.path.exists(dest):
            os.mkdir(dest)

        bst.save_model(os.path.join(dest, 'clf'))
        joblib.dump(scaler, os.path.join(dest, 'scaler.pkl'))

        return dest

# print(MLEngine().analyze())