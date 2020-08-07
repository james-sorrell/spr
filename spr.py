# -*- coding: utf-8 -*-
""" Scissors Paper Rock

This program is the Scissors Paper Rock (SPR) game written for the
IMC Development test. It utilises PyQt5 to provide a UI for 
a simple SPR game. The user may use the push buttons to select
what they want to throw, the cpu will randomly generate an action
and the scores will be tallied.

Program should be run as follows:
    python spr.py

Author: James Sorrell
"""

import sys
import time
import threading
import random
from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget, QInputDialog


class GameController(QtWidgets.QMainWindow, Ui_MainWindow):
    """ Game Controller Class
    This inherits from the generated MainWindow class and 
    provides additional functionality for controlling the 
    game as well as querying the user. 
    """ 
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

    def queryNumberOfGames(self):
        """ Query the user for how many games they'd like to play """
        i, okPressed = QInputDialog.getInt(self, "Games","How many games do you want to play?\n" \
        "The game will start immediately after this screen.\nSelect a throw option while the timer goes down!", 3, 0, 100, 1)
        if okPressed:
            self.games = i
            print("Games: {}".format(i))
        else:
            # TODO: Handle this properly, exiting
            # on failed input is poor user experience
            print("Fatal Error")
            quit()
    
    def setThrowButtons(self, setting):
        """ Disable buttons helper function """
        self.pushButton_1.setEnabled(setting)
        self.pushButton_2.setEnabled(setting)
        self.pushButton_3.setEnabled(setting)
        
    def generateCpuThrow(self):
        """ Generates and displays the CPU throw """
        self.cpuThrow = random.randint(0, 2)
        if (self.cpuThrow == 0):
            print("Cpu threw Scissors!")
            self.showCpuScissors()
        elif (self.cpuThrow == 1):
            print("Cpu threw Paper!")
            self.showCpuPaper()
        else:
            print("Cpu threw Rock!")
            self.showCpuRock()
        # Reveal the players throw
        if (self.playerThrow == 0):
            print("Player threw Scissors!")
            self.showScissors()
        elif (self.playerThrow == 1):
            print("Player threw Paper!")
            self.showPaper()
        else:
            print("Player threw Rock!")
            self.showRock()

    def checkResult(self):
        """ Determine who won, the player or the cpu """
        if (self.cpuThrow-1) % 3 == self.playerThrow:
            print("Player Wins!")
            self.setMiddleLabel("WINNER")
            self.playerScore += 1
        elif self.cpuThrow == self.playerThrow:
            self.setMiddleLabel("  DRAW")
            print("Draw")
        else:
            print("Cpu Wins!")
            self.setMiddleLabel(" LOSER")
            self.cpuScore += 1
        # Update the scoreboard in the ui
        self.setScores()

    def gameHandler(self):
        """ Handles the game timing and UI """
        # Reset player throw
        self.playerThrow = None
        # Enable throw buttons
        self.setThrowButtons(True)
        # Reset the middle label
        self.setMiddleLabel("IMC SPR")
        # Start the countdown timer
        self.setLabel("Scissors")
        time.sleep(1.5)
        self.setLabel("Paper...")
        time.sleep(1.5)
        # Wait for the player to throw something
        while self.playerThrow is None:
            print("Waiting for player to select a throw...")
            time.sleep(0.1)
        self.setLabel("Rock!")
        # Uncheck the selected throw button
        self.uncheckButton()
        # Disable throw buttons
        self.setThrowButtons(False)
        self.generateCpuThrow()
        self.checkResult()
        time.sleep(2)

    def runGames(self):
        """ Run through the provided number of games and control UI elements """
        print("Beginning the games!")
        for g in range(self.games):
            print("Starting game {}.".format(g))
            self.gameHandler()
            time.sleep(2)
        # Game is over, determine the overall winner
        if self.playerScore > self.cpuScore:
            print("Player is the big winner!")
            self.setFinalScreen("win")
        elif self.playerScore == self.cpuScore:
            print("It was all a draw!")
            self.setFinalScreen("draw")
        else:
            print("CPU wins! At least you're on the podium!")
            self.setFinalScreen("loss")

if __name__ == "__main__":
    """ Program Entry Point """

    print("Welcome to IMC SPR")    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GameController()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Query how many games the user
    # wants to play at start-up
    ui.queryNumberOfGames()

    # We need to run the game in seperate thread
    # so that the UI can still be used by the player    
    gameThread = threading.Thread(target=ui.runGames)
    gameThread.start()

    sys.exit(app.exec_())
