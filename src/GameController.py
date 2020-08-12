import threading
import time
import config as c

class GameController():
    """ Game Controller Class
    This class controls the game logic,
    it is passed in the ui controller 
    through it's constructor and uses it
    to interface with the ui.
    """ 
    def __init__(self, uic):
        # UI Controller
        self.uic = uic

    def start(self):
        """ Function will begin the game """
        self.numGames = self.uic.queryNumberOfGames()
        self.playerScore = 0
        self.cpuScore = 0
        # We need to run the Match in seperate thread
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
        # End the match and display end splash
        self.endMatch()

    def runGame(self):
        """ Ensures one game is run properly """
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
        self.checkResults()
        self.uic.setMiddleLabel(self.gameState)
        # Update the scoreboard in the ui
        self.uic.setScoreboard(self.playerScore, self.cpuScore)

    def endMatch(self):
        """ Check who won and display end screen """
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

    def checkResults(self):
        """ Determine who won, the player or the cpu """
        # This code is a big more difficult to understand but
        # the principle is simple, 
        #
        # Rock = 2
        # Paper = 1
        # Scissors = 0
        #
        # Note smaller number always beats the larger number
        # therefore, if we subtract one from one class and 
        # the numberas are the same, the class we subtracted
        # from would have lost. The modulus exists such that
        # we can 'wrap' the scissors class back to 2 -> (0-1)%3=2
        # 
        # Now we only need to check for two other states, draw
        # and the other player winning. Since it is easy to check
        # for a draw (classes are same) we should do this, then
        # all remaining states will be from the third class which
        # is CPU winning (as I checked for player winning first).
        #
        # Scores are updated on class variables
        #
        if (self.uic.cpuThrow-1) % 3 == self.uic.playerThrow:
            c.debugPrint("Player Wins!", 0)
            self.gameState="win"
            self.playerScore += 1
        elif self.uic.cpuThrow == self.uic.playerThrow:
            c.debugPrint("Draw", 0)
            self.gameState="draw"
        else:
            c.debugPrint("Cpu Wins!", 0)
            self.gameState="loss"
            self.cpuScore += 1
