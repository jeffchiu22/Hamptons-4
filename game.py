#Holds the game class
from player import *

class Game(object):
    def __init__(self, gameID, team1, team2, period=1, PCTime=7200):
        self.ID = gameID
        self.period, self.PCTime = period, PCTime
        self.team1, self.team2 = team1, team2

    #for debugging purposes
    def __repr__(self):
        return self.ID

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return (isinstance(other, Game) and (self.ID == other.ID))
 
    #updates time left in a quarter (in tenths of a second) with each passing event
    def updateTime(self, PCTime=7200, period=""):
        self.PCTime = PCTime
        if period != "": self.period = period

    #updates lineups at the beginning of a period
    def updateLineup(self, team1Lineup, team2Lineup):
        self.inGame = [team1Lineup, team2Lineup]

    #handles substitutions
    def substitution(self, playerIn, playerOut):
        if playerIn.team == self.team1:
            index = 0
        else:
            index = 1
        self.inGame[index].discard(playerOut)
        self.inGame[index].add(playerIn)