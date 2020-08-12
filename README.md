# SPR | Scissors Paper Rock

Scissors, paper, rock! with some PyQT5 UI.

## Design Overview

The UIController class provides an interface through
which the UI is modified. The MainWindow class contains
core functions and layouts for the Main Window. The
Game Controller class contains functions for controlling
the flow of the Match and executing the individual games.
It calls functions on the UIController to manipulate the 
UI and detect what hand the user has thrown.

## Trade Offs

I decided to opt for a user interface and that has come with
some sacrifices. Most notably, the UIController(UIC) holds variables 
which are needed for game operation in the game controller. This leads
to some difficulty due to multiple sources accessing the same
variables on different threads as well as code that is less clean.
In future if I was to productionise this concept I would reccomend
refactoring the code into something like MVVM such that there is 
a cleaner interface through which the front end and model can 
interact with each other. On the upside, I think this is visually
more impressive than a terminal window based scissors paper rock
game and that was the main motivation behind my decision to 
do it in this manner.

Secondly, in this code, the UIC controls the flow of each individual 
match as it holds the main thread in timed sleeps while a separate
thread is managing the UI. This is not ideal as we should not hold
the main thread idle if there is no need to do so. It would be 
better to run another thread that control the UI timing and 
visualisation so that the main thread is free. The reason I did 
not do this is that this opens up the program to timing issues 
and I felt that the added complexity would not add much benefit 
as there is not much else going on in the game. There may be other
good ways to do this and it could be worth consulting someone
with more UI/Game design experience.

> Instructions

Install Python 3.x
```
pip install -r requirements.txt
cd src
python spr.py
```