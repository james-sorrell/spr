# SPR | Scissors Paper Rock

Scissors, paper, rock! with some PyQT5 UI.

The UIController class provides an interface through
which the UI is modified. The MainWindow class contains
core functions and layouts for the Main Window. The
Game Controller class contains functions for controlling
the flow of the Match and executing the individual games.
It calls functions on the UIController to manipulate the 
UI and detect what hand the user has thrown.

> Instructions

Install Python 3.x
```
pip install -r requirements.txt
cd src
python spr.py
```