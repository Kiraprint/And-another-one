# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1121, 801))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_pb = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_pb.setObjectName("add_pb")
        self.verticalLayout.addWidget(self.add_pb)
        self.edit_pb = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.edit_pb.setObjectName("edit_pb")
        self.verticalLayout.addWidget(self.edit_pb)
        self.coffee_table = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.coffee_table.setObjectName("coffee_table")
        self.coffee_table.setColumnCount(0)
        self.coffee_table.setRowCount(0)
        self.verticalLayout.addWidget(self.coffee_table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_pb.setText(_translate("MainWindow", "Add coffee pack"))
        self.edit_pb.setText(_translate("MainWindow", "Edit cofee pack"))