# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'Form_ShowData.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form_ShowData(object):
    placeHolder = []
    def setupUi(self, Form_ShowData):
        Form_ShowData.setObjectName("Form_ShowData")
        Form_ShowData.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Form_ShowData)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 531, 171))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(7)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        Form_ShowData.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Form_ShowData)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        Form_ShowData.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Form_ShowData)
        self.statusbar.setObjectName("statusbar")
        Form_ShowData.setStatusBar(self.statusbar)

        self.retranslateUi(Form_ShowData)
        QtCore.QMetaObject.connectSlotsByName(Form_ShowData)
        print(self.placeHolder)

    def retranslateUi(self, Form_ShowData):
        _translate = QtCore.QCoreApplication.translate
        Form_ShowData.setWindowTitle(_translate("Form_ShowData", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form_ShowData", "NAME"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form_ShowData", "NPM"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form_ShowData", "CLASS"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form_ShowData", "GENDER"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form_ShowData", "ADDRESS"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form_ShowData", "STATUS"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form_ShowData", "HOBBY"))
