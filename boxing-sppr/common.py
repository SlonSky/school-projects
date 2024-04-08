from typing import Iterable

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from ui import main_window


def setup_boxers_table(table_obj):
    table_obj.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    table_obj.setColumnCount(9)
    table_obj.setHorizontalHeaderLabels([
        "ID", "Ім'я", "Вік", "Перемоги", "Нічиї", "Програші", "Пер.нокаутом", "Країна", "Досвід"
    ])


def setup_referee_table(table_obj):
    table_obj.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    table_obj.setColumnCount(3)
    table_obj.setHorizontalHeaderLabels([
        "ID", "Ім'я", "Країна"
    ])


def setup_place_table(table_obj):
    table_obj.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
    table_obj.setColumnCount(3)
    table_obj.setHorizontalHeaderLabels([
        "ID", "Назва", "Країна"
    ])


def add_to_table(row, table_obj, fields: Iterable):
    for i, field in fields:
        table_obj.setItem(row, i, QTableWidgetItem(field))

class Manager:

    def __init__(self, window: main_window.Ui_MainWindow):
        self.window = window

    def update_data(self):
        pass

    def _error_message(self, parent, text):
        mes = QtWidgets.QMessageBox(parent)
        mes.setIcon(QtWidgets.QMessageBox.Warning)
        mes.setText(text)
        mes.setWindowTitle("Помилка")
        mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = mes.exec_()

    def _get_selected_row_id(self, table):
        item = table.item(table.currentRow(), 0)
        if item is not None:
            return int(item.text())

    def _was_row_selected(self, table):
        return table.currentRow() != -1