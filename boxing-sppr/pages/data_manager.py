from collections import namedtuple

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from common import setup_referee_table, setup_place_table, setup_boxers_table, Manager
from db import DBManager, Boxer, Referee, Place
from ui import main_window, boxer_dialog, referee_dialog, place_dialog


class BoxerDialog(QtWidgets.QDialog, boxer_dialog.Ui_Dialog):
    def __init__(self, parent=None, boxer=None, title=None):
        super(BoxerDialog, self).__init__(parent)
        self.setupUi(self)

        if title is not None:
            self.setWindowTitle(title)

        if boxer is not None:
            self.age.setText(str(boxer.age))
            self.name.setText(boxer.name)
            self.won.setText(str(boxer.won))
            self.drawn.setText(str(boxer.drawn))
            self.kos.setText(str(boxer.kos))
            self.lost.setText(str(boxer.lost))
            self.experience.setText(str(boxer.experience))
            self.country.setText(boxer.country)

    def get_data(self):
        return Boxer(
            name=self.name.text(),
            age=int(self.age.text()),
            won=int(self.won.text()),
            drawn=int(self.drawn.text()),
            lost=int(self.lost.text()),
            kos=int(self.kos.text()),
            country=self.country.text(),
            experience=int(self.experience.text())
        )

class RefereeDialog(QtWidgets.QDialog, referee_dialog.Ui_Dialog):
    def __init__(self, parent=None, referee=None, title=None):
        super(RefereeDialog, self).__init__(parent)
        self.setupUi(self)

        if title is not None:
            self.setWindowTitle(title)

        if referee is not None:
            self.name.setText(referee.name)
            self.country.setText(referee.country)


    def get_data(self):
        return Referee(name=self.name.text(), country=self.country.text())


class PlaceDialog(QtWidgets.QDialog, place_dialog.Ui_Dialog):
    def __init__(self, parent=None, place=None, title=None):
        super(PlaceDialog, self).__init__(parent)
        self.setupUi(self)

        if title is not None:
            self.setWindowTitle(title)

        if place is not None:
            self.name.setText(place.name)
            self.country.setText(place.country)

    def get_data(self):
        return Place(name=self.name.text(), country=self.country.text())


class DataPageManager(Manager):


    def setup_db_page(self):

        self.db_manager = DBManager()

        setup_boxers_table(self.window.boxerTable)
        setup_referee_table(self.window.refereeTable)
        setup_place_table(self.window.placeTable)

        self.window.addRefereeBtn.clicked.connect(self._add_referee)
        self.window.editRefereeBtn.clicked.connect(self._edit_referee)
        self.window.deleteRefereeBtn.clicked.connect(self._delete_referee)

        self.window.addBoxerBtn.clicked.connect(self._add_boxer)
        self.window.editBoxerBtn.clicked.connect(self._edit_boxer)
        self.window.deleteBoxerBtn.clicked.connect(self._delete_boxer)

        self.window.addPlaceBtn.clicked.connect(self._add_place)
        self.window.editPlaceBtn.clicked.connect(self._edit_place)
        self.window.deletePlaceBtn.clicked.connect(self._delete_place)

        self.update_data()

    def update_data(self):
        self._load_db_boxers()
        self._load_db_referee()
        self._load_db_places()

    def _add_place(self):
        dialog = PlaceDialog(self.window, title="Додати місце")
        dialog.exec_()

        if dialog.result() == QtWidgets.QDialog.Rejected:
            return

        place = dialog.get_data()
        print(f"adding {place}")

        self.db_manager.add_place(place)
        self._load_db_places()
        self.window.update_trigger()

    def _edit_place(self):
        if self._was_row_selected(self.window.placeTable):
            place_id = self._get_selected_row_id(self.window.placeTable)
            place = self.db_manager.find_place(place_id)

            dialog = PlaceDialog(self.window, place, "Редагувати місце")
            dialog.exec_()

            if dialog.result() == QtWidgets.QDialog.Rejected:
                return

            edited_place = dialog.get_data()

            self.db_manager.update_place(place_id, edited_place)
            self._load_db_places()

            self.window.update_trigger()
        else:
            self._error_message(self.window, "Нічого не обрано")

    def _delete_place(self):
        if self._was_row_selected(self.window.placeTable):
            delete_id = self._get_selected_row_id(self.window.placeTable)
            self.db_manager.delete_place(delete_id)
            self._load_db_places()

            self.window.update_trigger()

    def _add_boxer(self):
        dialog = BoxerDialog(self.window, title="Додати боксера")
        dialog.exec_()

        if dialog.result() == QtWidgets.QDialog.Rejected:
            return

        boxer = dialog.get_data()
        print(f"adding {boxer}")

        self.db_manager.add_boxer(boxer)

        self._load_db_boxers()
        self.window.update_trigger()


    def _edit_boxer(self):
        if self._was_row_selected(self.window.boxerTable):
            boxer_id = self._get_selected_row_id(self.window.boxerTable)
            boxer = self.db_manager.find_boxer(boxer_id)

            dialog = BoxerDialog(self.window, boxer, "Редагувати боксера")
            dialog.exec_()

            if dialog.result() == QtWidgets.QDialog.Rejected:
                return

            edited_boxer = dialog.get_data()

            self.db_manager.update_boxer(boxer_id, edited_boxer)
            self._load_db_boxers()

            self.window.update_trigger()
        else:
            self._error_message(self.window, "Нічого не обрано")

    def _delete_boxer(self):
        if self._was_row_selected(self.window.boxerTable):
            delete_id = self._get_selected_row_id(self.window.boxerTable)
            DBManager().delete_boxer(delete_id)

            self._load_db_boxers()

            self.window.update_trigger()

    def _load_db_boxers(self):
        self._load(self.db_manager.find_all_boxers, self.window.boxerTable, ['id', 'name', 'age', 'won', 'lost', 'drawn', 'kos', 'country', 'experience'])

###################################

    def _add_referee(self):

        dialog = RefereeDialog(self.window, title="Додати рефері")
        dialog.exec_()

        if dialog.result() == QtWidgets.QDialog.Rejected:
            return

        referee = dialog.get_data()
        print(f"adding {referee}")

        self.db_manager.add_referee(referee)

        self._load_db_referee()

        self.window.update_trigger()

    def _edit_referee(self):

        if self._was_row_selected(self.window.refereeTable):
            referee_id = self._get_selected_row_id(self.window.refereeTable)
            referee = self.db_manager.find_referee(referee_id)

            dialog = RefereeDialog(self.window, referee, "Редагувати рефері")
            dialog.exec_()

            if dialog.result() == QtWidgets.QDialog.Rejected:
                return


            edited_referee = dialog.get_data()

            self.db_manager.update_referee(referee_id, edited_referee)
            self._load_db_referee()

            self.window.update_trigger()
        else:
            self._error_message(self.window, "Нічого не обрано")

    def _delete_referee(self):
        if self._was_row_selected(self.window.refereeTable):
            delete_id = self._get_selected_row_id(self.window.refereeTable)
            DBManager().delete_referee(delete_id)

            self._load_db_referee()

            self.window.update_trigger()

    def _load_db_referee(self):
        self._load(self.db_manager.find_all_referees, self.window.refereeTable, ['id', 'name', 'country'])

    def _load_db_places(self):
        self._load(self.db_manager.find_all_places, self.window.placeTable, ['id', 'name', 'country'])

    def _load(self, db_load, table, fields):
        entities = db_load()

        table.setRowCount(0)
        table.setRowCount(len(entities))

        for i, entity in enumerate(entities):
            for j, feature in enumerate(fields):
                table.setItem(i, j, QTableWidgetItem(str(getattr(entity, feature))))


