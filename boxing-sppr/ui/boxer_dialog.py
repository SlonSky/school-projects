# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'boxer_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(311, 520)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.age = QtWidgets.QLineEdit(Dialog)
        self.age.setObjectName("age")
        self.verticalLayout.addWidget(self.age)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.won = QtWidgets.QLineEdit(Dialog)
        self.won.setObjectName("won")
        self.verticalLayout.addWidget(self.won)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.drawn = QtWidgets.QLineEdit(Dialog)
        self.drawn.setObjectName("drawn")
        self.verticalLayout.addWidget(self.drawn)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.lost = QtWidgets.QLineEdit(Dialog)
        self.lost.setObjectName("lost")
        self.verticalLayout.addWidget(self.lost)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.kos = QtWidgets.QLineEdit(Dialog)
        self.kos.setObjectName("kos")
        self.verticalLayout.addWidget(self.kos)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.country = QtWidgets.QLineEdit(Dialog)
        self.country.setObjectName("country")
        self.verticalLayout.addWidget(self.country)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.experience = QtWidgets.QLineEdit(Dialog)
        self.experience.setObjectName("experience")
        self.verticalLayout.addWidget(self.experience)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_8.setText(_translate("Dialog", "Ім\'я"))
        self.label.setText(_translate("Dialog", "Вік"))
        self.label_2.setText(_translate("Dialog", "Перемоги"))
        self.label_3.setText(_translate("Dialog", "Нічиї"))
        self.label_4.setText(_translate("Dialog", "Програші"))
        self.label_5.setText(_translate("Dialog", "Перемоги нокаутом"))
        self.label_6.setText(_translate("Dialog", "Країна походження"))
        self.label_7.setText(_translate("Dialog", "Досвід"))
