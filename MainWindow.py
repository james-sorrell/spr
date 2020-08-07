# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow4.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#
# Edited by James Sorrell

from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.playerHand.setGeometry(QtCore.QRect(120, 140, 281, 281))
        self.playerHand.setText("")
        self.playerHand.setPixmap(QtGui.QPixmap("img/rock.png"))
        self.playerHand.setScaledContents(True)
        self.playerHand.setObjectName("playerHand")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(120, 420, 171, 51))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 420, 171, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 420, 171, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.cpuHand = QtWidgets.QLabel(self.centralwidget)
        self.cpuHand.setGeometry(QtCore.QRect(440, 0, 211, 191))
        self.cpuHand.setText("")
        self.cpuHand.setPixmap(QtGui.QPixmap("img/frock.png"))
        self.cpuHand.setScaledContents(True)
        self.cpuHand.setObjectName("cpuHand")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 301, 141))
        font = QtGui.QFont()
        font.setFamily("Vladimir Script")
        font.setPointSize(72)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scoreboard = QtWidgets.QLabel(self.centralwidget)
        self.scoreboard.setGeometry(QtCore.QRect(490, 290, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.scoreboard.setFont(font)
        self.scoreboard.setObjectName("scoreboard")
        self.middleLabel = QtWidgets.QLabel(self.centralwidget)
        self.middleLabel.setGeometry(QtCore.QRect(370, 340, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.middleLabel.setFont(font)
        self.middleLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.middleLabel.setObjectName("middleLabel")
        self.finalScreen = QtWidgets.QLabel(self.centralwidget)
        self.finalScreen.setGeometry(QtCore.QRect(110, 20, 571, 391))
        self.finalScreen.setText("")
        self.finalScreen.setObjectName("finalScreen")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect push buttons to functions that
        # will connect the images to their labels
        self.pushButton_1.clicked.connect(self.setScissors)
        self.pushButton_1.setCheckable(True)
        self.pushButton_2.clicked.connect(self.setPaper)
        self.pushButton_2.setCheckable(True)
        self.pushButton_3.clicked.connect(self.setRock)
        self.pushButton_3.setCheckable(True)

        # Make button group
        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.pushButton_1)
        self.buttonGroup.addButton(self.pushButton_2)
        self.buttonGroup.addButton(self.pushButton_3)

    def uncheckButton(self):
        """ Uncheck active button in button group """
        # TODO: Find a cleaner way to uncheck buttons
        self.buttonGroup.setExclusive(False)
        self.pushButton_1.setChecked(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_3.setChecked(False)
        self.buttonGroup.setExclusive(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPR"))
        self.pushButton_1.setText(_translate("MainWindow", "Scissors"))
        self.pushButton_2.setText(_translate("MainWindow", "Paper"))
        self.pushButton_3.setText(_translate("MainWindow", "Rock"))
        self.setLabel("")
        self.playerThrow = None
        self.playerScore = 0
        self.cpuScore = 0
        self.setScores()
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

    def setFinalScreen(self, state):
        """ Set the final screen image """
        if state == "win":
            self.finalScreen.setPixmap(QtGui.QPixmap("img/W.png"))
        elif state == "draw":
            self.finalScreen.setPixmap(QtGui.QPixmap("img/D.png"))
        else:
            self.finalScreen.setPixmap(QtGui.QPixmap("img/L.png"))
        self.finalScreen.setScaledContents(True)

    def setMiddleLabel(self, text):
        """ Sets the middle label below the scoreboard. """
        _translate = QtCore.QCoreApplication.translate
        self.middleLabel.setText(_translate("MainWindow", text))

    def setLabel(self, text):
        """ Sets the label used to display above player hand. """
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", text))

    def setScores(self):
        """ Sets the scoreboard based on the player/cpu scores """
        _translate = QtCore.QCoreApplication.translate
        scoreboardString = "{}-{}".format(str(self.playerScore), str(self.cpuScore))
        self.scoreboard.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreboard.setText(_translate("MainWindow", str(scoreboardString)))

    def setRock(self):
        """ Set player throw to rock """
        self.playerThrow = 2
        # self.pushButton_1.setStyleSheet("QPushButton::released")
        # self.pushButton_2.setStyleSheet("QPushButton::released")
        # self.pushButton_3.setStyleSheet("QPushButton::pressed")

    def showRock(self):
        """ Set rock image to player label """
        self.playerHand.setPixmap(QtGui.QPixmap("img/rock.png"))

    def showCpuRock(self):
        """ Set rock image to cpu label """
        self.cpuHand.setPixmap(QtGui.QPixmap("img/frock.png"))

    def setPaper(self):
        """ Set player throw to paper """
        self.playerThrow = 1 
        # self.pushButton_1.setStyleSheet("QPushButton::released")
        # self.pushButton_2.setStyleSheet("QPushButton::pressed")
        # self.pushButton_3.setStyleSheet("QPushButton::released")

    def showPaper(self):
        """ Set paper image to player label """
        self.playerHand.setPixmap(QtGui.QPixmap("img/paper.png"))

    def showCpuPaper(self):
        """ Set paper image to cpu label """
        self.cpuHand.setPixmap(QtGui.QPixmap("img/fpaper.png"))

    def setScissors(self):
        """ Set player throw to scissors """
        self.playerThrow = 0
        # self.pushButton_1.setStyleSheet("QPushButton::pressed")
        # self.pushButton_2.setStyleSheet("QPushButton::released")
        # self.pushButton_3.setStyleSheet("QPushButton::released")

    def showScissors(self):
        """ Set scissors image to player label """
        self.playerHand.setPixmap(QtGui.QPixmap("img/scissors.png"))
        
    
    def showCpuScissors(self):
        """ Set scissors image to cpu label """
        self.cpuHand.setPixmap(QtGui.QPixmap("img/fscissors.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
