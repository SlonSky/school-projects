import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView

from ui import main_window, boxer_dialog



class AddBoxerDialog(QtWidgets.QDialog, boxer_dialog.Ui_Dialog):

    # def __init__(self, parent=None):
    #     super(AddBoxerDialog, self).__init__(parent)
    #     self.setupUi(self)
    #
    # def get_data(self):
    #     return
    #
    def accept(self):
        print(f"hi, {self.lineEdit.text()}")

        super().accept()




class MyApp(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.trainClfBtn.clicked.connect(self.load_data_dialog)


        self.editBoxerBtn.clicked.connect(self.edit_boxer)

        # self.boxerTable.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.boxerTable.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.boxerTable.setColumnCount(3)
        self.boxerTable.setRowCount(50)
        self.boxerTable.setHorizontalHeaderLabels(["Age", "Won", "Stance"])


        for i in range(0, 50):
            self.boxerTable.setItem(i, 0, QTableWidgetItem("22"))
            self.boxerTable.setItem(i, 1, QTableWidgetItem("10"))
            self.boxerTable.setItem(i, 2, QTableWidgetItem("orthodox"))

    def edit_boxer(self):
        # dialog = AddBoxerDialog(self)
        dialog = AddBoxerDialog(self)
        res = dialog.exec_()
        print(dialog.myData())
        # self.boxerTable.setRowCount(5)
        # self.boxerTable.setHorizontalHeaderLabels(["Age", "Won", "Stance"])

        for i in range(0, 50):
            self.boxerTable.setItem(i, 0, QTableWidgetItem("00"))
            self.boxerTable.setItem(i, 1, QTableWidgetItem("8"))
            self.boxerTable.setItem(i, 2, QTableWidgetItem("orthodox"))

    # def chLabel(self):
    #     self.label.setText('You clicked')
    #     dlg = QtWidgets.QFileDialog()
    #     dlg.setFileMode(QtWidgets.QFileDialog.AnyFile)
    #
    #     if dlg.exec_():
    #         filenames = dlg.selectedFiles()
    #         f = open(filenames[0], 'r')
    #
    #         with f:
    #             data = f.read()
    #             self.contents.setText(data)

    def load_data_dialog(self):
        print('load data')
        mes = QtWidgets.QMessageBox()
        mes.setIcon(QtWidgets.QMessageBox.Warning)
        mes.setText("Wrong format")
        mes.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = mes.exec_()

    def loadClfDialog(self):
        print('clicked')
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            print(fileName)




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()