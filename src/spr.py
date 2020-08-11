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
from PyQt5 import QtWidgets
from UIController import UIController
import config as c

class GameController():
    """ Game Controller Class
    This class controls the game logic,
    it is passed in the ui controller 
    through it's constructor and uses it
    to interface with the ui.
    """ 
    def __init__(self, uic):
        self.uic = uic

    def start(self):
        """ Function will begin the game """
        self.numGames = self.uic.queryNumberOfGames()
        self.playerScore = 0
        self.cpuScore = 0
        # We need to run the game in seperate thread
        # so that the UI can still be used by the player    
        gameThread = threading.Thread(target=self.runMatch)
        gameThread.start()

    def runMatch(self):
        """ Run through the provided number of games and control UI elements """
        c.debugPrint("Beginning the games!", 0)
        for g in range(self.numGames):
            c.debugPrint("Starting game {}.".format(g), 1)
            self.runGame()
            # Sleep a little so that the next game doesn't start abruptly
            time.sleep(2)
        # Game is over, determine the overall winner
        if self.playerScore > self.cpuScore:
            c.debugPrint("Player is the big winner!", 0)
            self.uic.setFinalScreen("win")
        elif self.playerScore == self.cpuScore:
            c.debugPrint("It was all a draw!", 0)
            self.uic.setFinalScreen("draw")
        else:
            c.debugPrint("CPU wins! At least you're on the podium!", 0)
            self.uic.setFinalScreen("loss")

    def updateResults(self):
        """ Determine who won, the player or the cpu """
        if (self.uic.cpuThrow-1) % 3 == self.uic.playerThrow:
            c.debugPrint("Player Wins!", 0)
            self.uic.setMiddleLabel("WINNER")
            self.playerScore += 1
        elif self.uic.cpuThrow == self.uic.playerThrow:
            c.debugPrint("Draw", 0)
            self.uic.setMiddleLabel("  DRAW")
        else:
            c.debugPrint("Cpu Wins!", 0)
            self.uic.setMiddleLabel(" LOSER")
            self.cpuScore += 1

    def runGame(self):
        """ Ensures one game is run properly """
        # Reset player throw
        self.uic.playerThrow = None
        # UI Game Control - Begin Game
        self.uic.setToStartState()
        self.uic.beginCountdown()
        # Wait for the player to throw something
        # TODO: Polling isn't ideal
        while self.uic.playerThrow is None:
            c.debugPrint("Waiting for player to select a throw...", 2)
            time.sleep(0.1)
        # Set the UI to the post-game state
        self.uic.setToPostGame()
        # Check who won
        self.updateResults()
        # Update the scoreboard in the ui
        self.uic.setScoreboard(self.playerScore, self.cpuScore)


if __name__ == "__main__":
    """ Program Entry Point """

    print("Welcome to IMC SPR")    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    uic = UIController()
    uic.setupUi(MainWindow)
    MainWindow.show()

    gc = GameController(uic)
    gc.start()

    sys.exit(app.exec_())

