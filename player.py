#!/usr/bin/env python
from table import Table
from bet import Bet

class Player:
    
    def __init__(self, table: Table) -> None:
        self.table = table
        self.stake: int = 0
        self.wheel = self.table.wheel
        self.roundsToGo: int = 0
    
    def playing(self):
        if self.roundsToGo <= 0 or self.stake <= 0:
            return False
        if self.roundsToGo > 0 or self.stake > 0:
            return True
        False
        
    
    def placeBet(self):
        pass
    
    def win(self, bet: Bet):
        return bet.winAmount
    
    def lose(self, bet: Bet):
        pass