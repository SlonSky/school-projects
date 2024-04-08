import os
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from lightgbm.callback import _format_eval_result

from common import Manager
from ml import MLEngine
from ui import main_window


class TrainClfThread(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)

    def __init__(self, filename, ml_engine: MLEngine):
        super().__init__()
        self.filename = filename
        self.ml_engine = ml_engine

    def __del__(self):
        self.wait()

    def train_callback(self, env):
        period = 80
        if env.evaluation_result_list and (env.iteration + 1) % period == 0:
            result = '\t'.join([_format_eval_result(x, True) for x in env.evaluation_result_list])
            self.log_update.emit('[%d]\t%s' % (env.iteration + 1, result))

    def run(self):

        try:
            df = self.ml_engine.read_train_data(self.filename)

            self.progress_update.emit(13)
            self.log_update.emit("Дані завантажено")

            df, test_df = self.ml_engine.split_train_test(df)

            self.progress_update.emit(26)
            self.log_update.emit("Створено навчальну та тестову виборки")

            df, test_df = self.ml_engine.categorize_data(df, test_df)

            self.progress_update.emit(39)
            self.log_update.emit("Дані категоризовано")

            scaler, X_train, Y_train, X_test, Y_test = self.ml_engine.normalize_data(df, test_df)

            self.progress_update.emit(51)
            self.log_update.emit("Дані нормалізовано. Починається навчання")

            bst = self.ml_engine.train_clf(X_train, Y_train, X_test, Y_test, self.train_callback)

            self.progress_update.emit(80)
            self.log_update.emit("Класифікатор натреновано. Починається тестування")

            report = self.ml_engine.estimate_clf(bst, X_test, Y_test)

            self.progress_update.emit(90)
            self.log_update.emit("Класифікатор протестовано. Результати:")
            self.log_update.emit(report)

            dirname = os.path.dirname(self.filename)
            dest = self.ml_engine.save_clf(bst, scaler, dirname)

            self.progress_update.emit(100)
            self.log_update.emit(f"Класифікатор збережено в директорії {dest}\n")

        except Exception as e:
            self.progress_update.emit(0)
            self.log_update.emit(f"\nПомилка: {e}\n")


class LoadClfThread(QThread):
    progress_update = pyqtSignal(int)
    log_update = pyqtSignal(str)
    load_complete = pyqtSignal(bool)

    def __init__(self, filename, ml_engine):
        super().__init__()
        self.dirname = filename
        self.ml_engine = ml_engine

    def __del__(self):
        self.wait()

    def run(self):
        print(self.dirname)

        clf_file = os.path.join(self.dirname, 'clf')
        scaler_file = os.path.join(self.dirname, 'scaler.pkl')
        if not (os.path.exists(clf_file) and os.path.isfile(clf_file)) or not (os.path.exists(scaler_file) and os.path.isfile(scaler_file)):
            self.log_update.emit("Не знайдено файл класифікатору.")
            return

        self.progress_update.emit(33)
        self.log_update.emit("Файли знайдено.")

        self.ml_engine.load_clf(clf_file)
        self.progress_update.emit(66)
        self.log_update.emit("Завантажено класифікатор.")

        self.ml_engine.load_scaler(scaler_file)
        self.progress_update.emit(100)
        self.log_update.emit("Завантажено масшатабувач.\n")

        self.load_complete.emit(True)


class ClfPageManager(Manager):

    def setup_classifier_page(self):
        self._update_clf_name()
        self.window.trainClfBtn.clicked.connect(self._train_classifier)
        self.window.loadClfBtn.clicked.connect(self._load_classifier)

        self.load_thread = None
        self.train_thread = None

    def _get_current_classifier(self):
        return self.window.ml_engine.clf_name or "Необхідно завантажити"

    def _train_classifier(self):


        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self.window,
            "Оберіть файл з даними", "", "Файл з родільниками (*.csv)",
            options=options
        )

        if filename and (
            self.train_thread is None
            or not self.train_thread.isRunning()
        ):
            self.train_thread = TrainClfThread(filename, self.window.ml_engine)
            self.train_thread.progress_update.connect(self._update_clf_progress_bar)
            self.train_thread.log_update.connect(self._update_clf_log)

            self.train_thread.start()

    def _load_classifier(self):

        dirname = QtWidgets.QFileDialog.getExistingDirectory(self.window, "Оберіть директорію з класифікатором")
        if dirname and (
                self.load_thread is None
                or not self.load_thread.isRunning()
        ):
            self.load_thread = LoadClfThread(dirname, self.window.ml_engine)
            self.load_thread.start()
            self.load_thread.progress_update.connect(self._update_clf_progress_bar)
            self.load_thread.log_update.connect(self._update_clf_log)
            self.load_thread.load_complete.connect(self._update_clf_name)

    def _update_clf_name(self, v=None):
            self.window.clfLabel.setText(self._get_current_classifier())

    def _update_clf_progress_bar(self, value):
        self.window.clfProgress.setValue(value)

    def _update_clf_log(self, log):
        self.window.clfLog.append(log)


