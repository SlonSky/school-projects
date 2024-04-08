import sys

from PyQt5 import QtWidgets

from ml import MLEngine
from pages.clf_manager import ClfPageManager
from pages.data_manager import DataPageManager
from db import DBManager
from ui import main_window
from pages.work_manager import WorkPageManager


class MainApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("СППР")

        self.ml_engine = MLEngine()

        self.clf_page_manager = ClfPageManager(self)
        self.clf_page_manager.setup_classifier_page()

        self.data_page_manager = DataPageManager(self)
        self.data_page_manager.setup_db_page()

        self.work_page_manager = WorkPageManager(self)
        self.work_page_manager.setup_process_page()


    def update_trigger(self):
        self.clf_page_manager.update_data()
        self.data_page_manager.update_data()
        self.work_page_manager.update_data()


def main():
    DBManager.start()

    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

    DBManager.exit()


if __name__ == '__main__':
    main()

