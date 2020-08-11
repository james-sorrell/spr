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
from PyQt5 import QtWidgets
from UIController import UIController
from GameController import GameController
import config as c

def main():
    """ Main pipeline for program operation """

    c.debugPrint("Welcome to IMC SPR", 0)    
    
    # Open UI
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    uic = UIController()
    uic.setupUi(MainWindow)
    MainWindow.show()

    # Start Game
    gc = GameController(uic)
    gc.start()

    # Close UI
    sys.exit(app.exec_())

if __name__ == "__main__":
    """ Program Entry Point """
    main()
