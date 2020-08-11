import time
import random
from MainWindow import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog
import config as c

class UIController(QtWidgets.QMainWindow, Ui_MainWindow):
    """ UI Controller Class
    This inherits from the generated MainWindow class and 
    provides functionality for controlling the user interface.
    """
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

    def queryNumberOfGames(self):
        """ Query the user for how many games they'd like to play """
        i, okPressed = QInputDialog.getInt(self, "Games","How many games do you want to play?\n" \
        "The game will start immediately after this screen.\nSelect a throw option while the timer goes down!", 3, 0, 100, 1)
        if okPressed:
            c.debugPrint("Games: {}".format(i), 1)
            return i
        else:
            # TODO: Handle this properly, exiting
            # on failed input is poor user experience
            print("Fatal Error")
            quit()

    def setToStartState(self):
        """ Set game to start state """
        self.playerThrow = None
        self.setThrowButtons(True)
        self.setMiddleLabel()
        self.showRock()
        self.showCpuRock()

    def beginCountdown(self):
        """ Begin the visualisation of countdown timer """
        # Start the countdown timer
        self.setLabel("Scissors")
        time.sleep(1.5)
        self.setLabel("Paper...")
        time.sleep(1.5)

    def setThrowButtons(self, setting):
        """ Disable buttons helper function """
        self.pushButton_1.setEnabled(setting)
        self.pushButton_2.setEnabled(setting)
        self.pushButton_3.setEnabled(setting)
        
    def setToPostGame(self):
        self.setLabel("Rock!")
        # Uncheck the selected throw button
        self.uncheckButton()
        # Disable throw buttons
        self.setThrowButtons(False)
        self.generateAndDisplayThrows()

    def generateAndDisplayThrows(self):
        """ Generates and displays the CPU throw """
        self.cpuThrow = random.randint(0, 2)
        if (self.cpuThrow == 0):
            c.debugPrint("Cpu threw Scissors!", 1)
            self.showCpuScissors()
        elif (self.cpuThrow == 1):
            c.debugPrint("Cpu threw Paper!", 1)
            self.showCpuPaper()
        else:
            c.debugPrint("Cpu threw Rock!", 1)
            self.showCpuRock()
        # Reveal the players throw
        if (self.playerThrow == 0):
            c.debugPrint("Player threw Scissors!", 1)
            self.showScissors()
        elif (self.playerThrow == 1):
            c.debugPrint("Player threw Paper!", 1)
            self.showPaper()
        else:
            c.debugPrint("Player threw Rock!", 1)
            self.showRock()
