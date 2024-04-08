# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.clf_tab = QtWidgets.QWidget()
        self.clf_tab.setObjectName("clf_tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.clf_tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.clfLog = QtWidgets.QTextBrowser(self.clf_tab)
        self.clfLog.setObjectName("clfLog")
        self.gridLayout_3.addWidget(self.clfLog, 1, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.clf_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.clfLabel = QtWidgets.QLabel(self.clf_tab)
        self.clfLabel.setObjectName("clfLabel")
        self.horizontalLayout_4.addWidget(self.clfLabel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.loadClfBtn = QtWidgets.QPushButton(self.clf_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadClfBtn.sizePolicy().hasHeightForWidth())
        self.loadClfBtn.setSizePolicy(sizePolicy)
        self.loadClfBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loadClfBtn.setObjectName("loadClfBtn")
        self.verticalLayout_3.addWidget(self.loadClfBtn)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.trainClfBtn = QtWidgets.QPushButton(self.clf_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trainClfBtn.sizePolicy().hasHeightForWidth())
        self.trainClfBtn.setSizePolicy(sizePolicy)
        self.trainClfBtn.setObjectName("trainClfBtn")
        self.gridLayout_3.addWidget(self.trainClfBtn, 0, 0, 1, 1)
        self.clfProgress = QtWidgets.QProgressBar(self.clf_tab)
        self.clfProgress.setProperty("value", 0)
        self.clfProgress.setObjectName("clfProgress")
        self.gridLayout_3.addWidget(self.clfProgress, 2, 1, 1, 1)
        self.tabWidget.addTab(self.clf_tab, "")
        self.db_tab = QtWidgets.QWidget()
        self.db_tab.setObjectName("db_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.db_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.db_tab)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 281, 121))
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBoxerBtn = QtWidgets.QPushButton(self.page)
        self.addBoxerBtn.setObjectName("addBoxerBtn")
        self.horizontalLayout.addWidget(self.addBoxerBtn)
        self.editBoxerBtn = QtWidgets.QPushButton(self.page)
        self.editBoxerBtn.setObjectName("editBoxerBtn")
        self.horizontalLayout.addWidget(self.editBoxerBtn)
        self.deleteBoxerBtn = QtWidgets.QPushButton(self.page)
        self.deleteBoxerBtn.setObjectName("deleteBoxerBtn")
        self.horizontalLayout.addWidget(self.deleteBoxerBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.boxerTable = QtWidgets.QTableWidget(self.page)
        self.boxerTable.setObjectName("boxerTable")
        self.boxerTable.setColumnCount(0)
        self.boxerTable.setRowCount(0)
        self.verticalLayout.addWidget(self.boxerTable)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 796, 412))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addRefereeBtn = QtWidgets.QPushButton(self.page_2)
        self.addRefereeBtn.setObjectName("addRefereeBtn")
        self.horizontalLayout_2.addWidget(self.addRefereeBtn)
        self.editRefereeBtn = QtWidgets.QPushButton(self.page_2)
        self.editRefereeBtn.setObjectName("editRefereeBtn")
        self.horizontalLayout_2.addWidget(self.editRefereeBtn)
        self.deleteRefereeBtn = QtWidgets.QPushButton(self.page_2)
        self.deleteRefereeBtn.setObjectName("deleteRefereeBtn")
        self.horizontalLayout_2.addWidget(self.deleteRefereeBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.refereeTable = QtWidgets.QTableWidget(self.page_2)
        self.refereeTable.setObjectName("refereeTable")
        self.refereeTable.setColumnCount(0)
        self.refereeTable.setRowCount(0)
        self.verticalLayout_2.addWidget(self.refereeTable)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 281, 121))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addPlaceBtn = QtWidgets.QPushButton(self.page_3)
        self.addPlaceBtn.setObjectName("addPlaceBtn")
        self.horizontalLayout_3.addWidget(self.addPlaceBtn)
        self.editPlaceBtn = QtWidgets.QPushButton(self.page_3)
        self.editPlaceBtn.setObjectName("editPlaceBtn")
        self.horizontalLayout_3.addWidget(self.editPlaceBtn)
        self.deletePlaceBtn = QtWidgets.QPushButton(self.page_3)
        self.deletePlaceBtn.setObjectName("deletePlaceBtn")
        self.horizontalLayout_3.addWidget(self.deletePlaceBtn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.placeTable = QtWidgets.QTableWidget(self.page_3)
        self.placeTable.setObjectName("placeTable")
        self.placeTable.setColumnCount(0)
        self.placeTable.setRowCount(0)
        self.verticalLayout_4.addWidget(self.placeTable)
        self.toolBox.addItem(self.page_3, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.db_tab, "")
        self.work_tab = QtWidgets.QWidget()
        self.work_tab.setObjectName("work_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.work_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.work_tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.deleteSelectedBoxerBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteSelectedBoxerBtn.sizePolicy().hasHeightForWidth())
        self.deleteSelectedBoxerBtn.setSizePolicy(sizePolicy)
        self.deleteSelectedBoxerBtn.setObjectName("deleteSelectedBoxerBtn")
        self.gridLayout_4.addWidget(self.deleteSelectedBoxerBtn, 0, 2, 1, 1)
        self.addSelectedBoxerBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSelectedBoxerBtn.sizePolicy().hasHeightForWidth())
        self.addSelectedBoxerBtn.setSizePolicy(sizePolicy)
        self.addSelectedBoxerBtn.setObjectName("addSelectedBoxerBtn")
        self.gridLayout_4.addWidget(self.addSelectedBoxerBtn, 0, 1, 1, 1)
        self.boxerSelector = QtWidgets.QComboBox(self.groupBox)
        self.boxerSelector.setObjectName("boxerSelector")
        self.gridLayout_4.addWidget(self.boxerSelector, 0, 0, 1, 1)
        self.selectedBoxersTable = QtWidgets.QTableWidget(self.groupBox)
        self.selectedBoxersTable.setObjectName("selectedBoxersTable")
        self.selectedBoxersTable.setColumnCount(0)
        self.selectedBoxersTable.setRowCount(0)
        self.gridLayout_4.addWidget(self.selectedBoxersTable, 2, 0, 1, 3)
        self.gridLayout_8.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.work_tab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.placeSelector = QtWidgets.QComboBox(self.groupBox_4)
        self.placeSelector.setObjectName("placeSelector")
        self.gridLayout_7.addWidget(self.placeSelector, 0, 0, 1, 1)
        self.addSelectedPlaceBtn = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSelectedPlaceBtn.sizePolicy().hasHeightForWidth())
        self.addSelectedPlaceBtn.setSizePolicy(sizePolicy)
        self.addSelectedPlaceBtn.setObjectName("addSelectedPlaceBtn")
        self.gridLayout_7.addWidget(self.addSelectedPlaceBtn, 0, 1, 1, 1)
        self.deleteSelectedPlaceBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.deleteSelectedPlaceBtn.setObjectName("deleteSelectedPlaceBtn")
        self.gridLayout_7.addWidget(self.deleteSelectedPlaceBtn, 0, 2, 1, 1)
        self.selectedPlaceTable = QtWidgets.QTableWidget(self.groupBox_4)
        self.selectedPlaceTable.setObjectName("selectedPlaceTable")
        self.selectedPlaceTable.setColumnCount(0)
        self.selectedPlaceTable.setRowCount(0)
        self.gridLayout_7.addWidget(self.selectedPlaceTable, 1, 0, 1, 3)
        self.gridLayout_8.addWidget(self.groupBox_4, 0, 2, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.work_tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox_3)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_6.addWidget(self.dateEdit, 0, 0, 1, 1)
        self.addDateBtn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDateBtn.sizePolicy().hasHeightForWidth())
        self.addDateBtn.setSizePolicy(sizePolicy)
        self.addDateBtn.setObjectName("addDateBtn")
        self.gridLayout_6.addWidget(self.addDateBtn, 0, 1, 1, 1)
        self.deleteSelectedDateBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.deleteSelectedDateBtn.setObjectName("deleteSelectedDateBtn")
        self.gridLayout_6.addWidget(self.deleteSelectedDateBtn, 0, 2, 1, 1)
        self.selectedDatesTable = QtWidgets.QListWidget(self.groupBox_3)
        self.selectedDatesTable.setObjectName("selectedDatesTable")
        self.gridLayout_6.addWidget(self.selectedDatesTable, 1, 0, 1, 3)
        self.gridLayout_8.addWidget(self.groupBox_3, 1, 2, 1, 1)
        self.analyzeProgress = QtWidgets.QProgressBar(self.work_tab)
        self.analyzeProgress.setProperty("value", 0)
        self.analyzeProgress.setObjectName("analyzeProgress")
        self.gridLayout_8.addWidget(self.analyzeProgress, 2, 1, 1, 2)
        self.analyzeBtn = QtWidgets.QPushButton(self.work_tab)
        self.analyzeBtn.setObjectName("analyzeBtn")
        self.gridLayout_8.addWidget(self.analyzeBtn, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.work_tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.refereeSelector = QtWidgets.QComboBox(self.groupBox_2)
        self.refereeSelector.setObjectName("refereeSelector")
        self.gridLayout_5.addWidget(self.refereeSelector, 0, 0, 1, 1)
        self.addSelectedRefereeBtn = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSelectedRefereeBtn.sizePolicy().hasHeightForWidth())
        self.addSelectedRefereeBtn.setSizePolicy(sizePolicy)
        self.addSelectedRefereeBtn.setObjectName("addSelectedRefereeBtn")
        self.gridLayout_5.addWidget(self.addSelectedRefereeBtn, 0, 1, 1, 1)
        self.deleteSelectedRefereeBtn = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteSelectedRefereeBtn.sizePolicy().hasHeightForWidth())
        self.deleteSelectedRefereeBtn.setSizePolicy(sizePolicy)
        self.deleteSelectedRefereeBtn.setObjectName("deleteSelectedRefereeBtn")
        self.gridLayout_5.addWidget(self.deleteSelectedRefereeBtn, 0, 2, 1, 1)
        self.selectedRefereeTable = QtWidgets.QTableWidget(self.groupBox_2)
        self.selectedRefereeTable.setObjectName("selectedRefereeTable")
        self.selectedRefereeTable.setColumnCount(0)
        self.selectedRefereeTable.setRowCount(0)
        self.gridLayout_5.addWidget(self.selectedRefereeTable, 1, 0, 1, 3)
        self.gridLayout_8.addWidget(self.groupBox_2, 1, 0, 1, 2)
        self.tabWidget.addTab(self.work_tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.clf_tab.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.clfLog.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Журнал</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Класифікатор:"))
        self.clfLabel.setText(_translate("MainWindow", "TextLabel"))
        self.loadClfBtn.setText(_translate("MainWindow", "Завантажити"))
        self.trainClfBtn.setText(_translate("MainWindow", "Натренувати"))
        self.clfProgress.setFormat(_translate("MainWindow", "Прогрес"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.clf_tab), _translate("MainWindow", "Класифікатор"))
        self.addBoxerBtn.setText(_translate("MainWindow", "Додати"))
        self.editBoxerBtn.setText(_translate("MainWindow", "Редагувати"))
        self.deleteBoxerBtn.setText(_translate("MainWindow", "Видалити"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Боксери"))
        self.addRefereeBtn.setText(_translate("MainWindow", "Додати"))
        self.editRefereeBtn.setText(_translate("MainWindow", "Редагувати"))
        self.deleteRefereeBtn.setText(_translate("MainWindow", "Видалити"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Рефері"))
        self.addPlaceBtn.setText(_translate("MainWindow", "Додати"))
        self.editPlaceBtn.setText(_translate("MainWindow", "Редагувати"))
        self.deletePlaceBtn.setText(_translate("MainWindow", "Видалити"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Місця"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.db_tab), _translate("MainWindow", "База даних"))
        self.groupBox.setTitle(_translate("MainWindow", "Боксери"))
        self.deleteSelectedBoxerBtn.setText(_translate("MainWindow", "Видалити"))
        self.addSelectedBoxerBtn.setText(_translate("MainWindow", "Додати"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Місця"))
        self.addSelectedPlaceBtn.setText(_translate("MainWindow", "Додати"))
        self.deleteSelectedPlaceBtn.setText(_translate("MainWindow", "Видалити"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Дати"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd.MM.yyyy"))
        self.addDateBtn.setText(_translate("MainWindow", "Додати"))
        self.deleteSelectedDateBtn.setText(_translate("MainWindow", "Видалити"))
        self.analyzeProgress.setFormat(_translate("MainWindow", "Прогрес"))
        self.analyzeBtn.setText(_translate("MainWindow", "Аналізувати"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Рефері"))
        self.addSelectedRefereeBtn.setText(_translate("MainWindow", "Додати"))
        self.deleteSelectedRefereeBtn.setText(_translate("MainWindow", "Видалити"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.work_tab), _translate("MainWindow", "Рішення"))