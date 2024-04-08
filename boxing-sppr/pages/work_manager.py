import time
from typing import List, Dict

from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QTableWidgetItem

from common import setup_boxers_table, setup_referee_table, setup_place_table, Manager
from db import DBManager, Place, Referee, Boxer
from ml import MLEngine
from ui import main_window, result_dialog


class ResultDialog(QtWidgets.QDialog, result_dialog.Ui_Dialog):
    def __init__(self, parent=None, result=None):
        super(ResultDialog, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Результати")

        self.resultTable.setColumnCount(6)
        self.resultTable.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.resultTable.setHorizontalHeaderLabels([
            "Перший боксер", "Другий боксер", "Рефері", "Місце", "Дата", "Невизначеність"
        ])
        self.resultTable.setRowCount(0)
        self.resultTable.setRowCount(len(result))

        for i, entry in enumerate(result):
            for j, field in enumerate(['boxer_a_name', 'boxer_b_name', 'referee_name', 'place_name', 'date', 'Uncert']):
                self.resultTable.setItem(i, j, QTableWidgetItem(str(entry.get(field))))



class AnalyzeThread(QThread):
    progress_update = pyqtSignal(int)
    result = pyqtSignal(list)

    def __init__(self, boxers, referees, places, dates, ml_engine: MLEngine):
        super().__init__()
        self.boxers = boxers
        self.referees = referees
        self.places = places
        self.dates = dates
        self.ml_engine = ml_engine

    def __del__(self):
        self.wait()

    def run(self):

        df = self.ml_engine.prepare_data(self.boxers, self.referees, self.places, self.dates)

        self.progress_update.emit(20)

        X, info = self.ml_engine.normalize_work_data(df)

        self.progress_update.emit(40)

        Y = self.ml_engine.predict_work_data(X)

        self.progress_update.emit(60)

        uncertanity = self.ml_engine.calc_uncert(Y)

        self.progress_update.emit(80)

        result = self.ml_engine.prepare_result(info, uncertanity)

        self.progress_update.emit(100)

        self.result.emit(result)


class WorkPageManager(Manager):

    def setup_process_page(self):

        self.db_manager = DBManager()

        setup_boxers_table(self.window.selectedBoxersTable)
        setup_referee_table(self.window.selectedRefereeTable)
        setup_place_table(self.window.selectedPlaceTable)

        self.update_data()

        self.window.addSelectedBoxerBtn.clicked.connect(self._add_selected_boxer)
        self.window.addSelectedRefereeBtn.clicked.connect(self._add_selected_referee)
        self.window.addSelectedPlaceBtn.clicked.connect(self._add_selected_place)
        self.window.addDateBtn.clicked.connect(self._add_date)

        self.window.deleteSelectedBoxerBtn.clicked.connect(self._delete_selected_boxer)
        self.window.deleteSelectedRefereeBtn.clicked.connect(self._delete_selected_referee)
        self.window.deleteSelectedPlaceBtn.clicked.connect(self._delete_selected_place)
        self.window.deleteSelectedDateBtn.clicked.connect(self._delete_selected_date)

        self.window.analyzeBtn.clicked.connect(self._analyze)

        self._analyze_thread = None


    ############## TODO: try with labmda

    def _add_from_selector(self, selector, table, fields, db_find):
        entity_id = selector.itemData(selector.currentIndex())
        entity = db_find(entity_id)

        rows_amt = table.rowCount()

        if entity_id is None or entity_id in [int(table.item(i, 0).text()) for i in range(rows_amt)]:
            return

        table.setRowCount(rows_amt + 1)

        for i, field in enumerate(fields):
            table.setItem(rows_amt, i, QTableWidgetItem(str(getattr(entity, field))))

    def _add_selected_boxer(self):
        self._add_from_selector(self.window.boxerSelector, self.window.selectedBoxersTable, ['id', 'name', 'age', 'won', 'lost', 'drawn', 'kos', 'country', 'experience'], self.db_manager.find_boxer)


    
    def _add_selected_referee(self):
        self._add_from_selector(self.window.refereeSelector, self.window.selectedRefereeTable,
                                ['id', 'name', 'country'],
                                self.db_manager.find_referee)

    def _add_selected_place(self):
        self._add_from_selector(self.window.placeSelector, self.window.selectedPlaceTable,
                                ['id', 'name', 'country'],
                                self.db_manager.find_place)

    def _add_date(self):
        date = self.window.dateEdit.text()

        if date not in [self.window.selectedDatesTable.item(i).text() for i in range(self.window.selectedDatesTable.count())]:
            self.window.selectedDatesTable.addItem(date)

    #################

    def _delete_selected_boxer(self):
        row = self.window.selectedBoxersTable.currentRow()
        self.window.selectedBoxersTable.removeRow(row)

    def _delete_selected_referee(self):
        row = self.window.selectedRefereeTable.currentRow()
        self.window.selectedRefereeTable.removeRow(row)

    def _delete_selected_place(self):
        row = self.window.selectedPlaceTable.currentRow()
        self.window.selectedPlaceTable.removeRow(row)

    def _delete_selected_date(self):
        row = self.window.selectedDatesTable.currentRow()
        self.window.selectedDatesTable.takeItem(row)

    ################

    def _get_table_ids(self, table):
        return [int(table.item(i, 0).text()) for i in range(table.rowCount())]

    def _analyze(self):

        if self.window.ml_engine.clf is None:
            self._error_message(self.window, "Спочатку необхідно завантажити класифікатоор")
            return

        if self.window.selectedBoxersTable.rowCount() == 0:
            self._error_message(self.window, 'Не обрано жодного боксера')
            return

        if self.window.selectedRefereeTable.rowCount() == 0:
            self._error_message(self.window, 'Не обрано жодного рефері')
            return

        if self.window.selectedPlaceTable.rowCount() == 0:
            self._error_message(self.window, 'Не обрано жодного місця')
            return

        if self.window.selectedDatesTable.count() == 0:
            self._error_message(self.window, 'Не обрано жодної дати')
            return

        boxers = [self.db_manager.find_boxer(i) for i in self._get_table_ids(self.window.selectedBoxersTable)]
        referees = [self.db_manager.find_referee(i) for i in self._get_table_ids(self.window.selectedRefereeTable)]
        places = [self.db_manager.find_place(i) for i in self._get_table_ids(self.window.selectedPlaceTable)]
        dates = [self.window.selectedDatesTable.item(i).text() for i in range(self.window.selectedDatesTable.count())]

        if len(boxers) < 2:
            self._error_message(self.window, "Оберіть принаймні двох боксерів")
            return

        if self._analyze_thread is None or not self._analyze_thread.isRunning():
            self._analyze_thread = AnalyzeThread(boxers, referees, places, dates, self.window.ml_engine)
            self._analyze_thread.start()
            self._analyze_thread.progress_update.connect(lambda x: self.window.analyzeProgress.setValue(x))
            self._analyze_thread.result.connect(self._show_result)

    def _show_result(self, data: List[Dict]):
        dialog = ResultDialog(self.window, result=data)
        dialog.exec_()

    def update_data(self):
        self._load_boxer_selector()
        self._load_place_selector()
        self._load_referee_selector()

    def _load_boxer_selector(self):

        self.window.boxerSelector.clear()
        boxers = self.db_manager.find_all_boxers()
        for i in boxers:
            self.window.boxerSelector.addItem(i.name, i.id)

    def _load_referee_selector(self):

        self.window.refereeSelector.clear()
        referees = self.db_manager.find_all_referees()
        for i in referees:
            self.window.refereeSelector.addItem(i.name, i.id)


    def _load_place_selector(self):

        self.window.placeSelector.clear()
        places = self.db_manager.find_all_places()
        for i in places:
            self.window.placeSelector.addItem(i.name, i.id)
