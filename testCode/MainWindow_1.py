# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# PyQt5 UI Generator used to set the general layout
# modifications that carry functionality were made
# manually.
#
# Edited by: James Sorrell

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/lgoo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.playerHand = QtWidgets.QLabel(self.centralwidget)
        self.playerHand.setGeometry(QtCore.QRect(120, 180, 281, 281))
        self.playerHand.setText("")
        self.playerHand.setPixmap(QtGui.QPixmap("img/rock.png"))
        self.playerHand.setScaledContents(True)
        self.playerHand.setObjectName("playerHand")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(120, 460, 171, 51))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 460, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 460, 171, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.cpuHand = QtWidgets.QLabel(self.centralwidget)
        self.cpuHand.setGeometry(QtCore.QRect(440, 40, 211, 191))
        self.cpuHand.setText("")
        self.cpuHand.setPixmap(QtGui.QPixmap("img/frock.png"))
        self.cpuHand.setScaledContents(True)
        self.cpuHand.setObjectName("cpuHand")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.menuFile.addAction(self.actionNew)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect push buttons to functions that
        # will connect the images to their labels
        self.pushButton_1.clicked.connect(self.showRock)
        self.pushButton_2.clicked.connect(self.showPaper)
        self.pushButton_3.clicked.connect(self.showScissors)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPR"))
        self.pushButton_1.setText(_translate("MainWindow", "Rock"))
        self.pushButton_2.setText(_translate("MainWindow", "Paper"))
        self.pushButton_3.setText(_translate("MainWindow", "Scissors"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

    def showRock(self):
        ''' Set rock image to player label '''
        self.playerHand.setPixmap(QtGui.QPixmap("img/rock.png"))
        self.cpuHand.setPixmap(QtGui.QPixmap("img/frock.png"))

    def showPaper(self):
        ''' Set paper image to player label '''
        self.playerHand.setPixmap(QtGui.QPixmap("img/paper.png"))
        self.cpuHand.setPixmap(QtGui.QPixmap("img/fpaper.png"))

    def showScissors(self):
        ''' Set scissors image to player label '''
        self.playerHand.setPixmap(QtGui.QPixmap("img/scissors.png"))
        self.cpuHand.setPixmap(QtGui.QPixmap("img/fscissors.png"))
