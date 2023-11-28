#!/usr/bin/env python
from table import Table
from bet import Bet
from outcome import PrisonOutcome

class Player:
    
    def __init__(self, table: Table) -> None:
        self.table = table
        self.stake: int = 0
        self.wheel = self.table.wheel
        self.roundsToGo: int = 5
    
    def playing(self):
        if self.roundsToGo <= 0 or self.stake <= 0:
            return False
        if self.roundsToGo > 0 or self.stake > 0:
            return True
        False
        
    
    def placeBet(self):
        pass
    
    def win(self, bet: Bet):
        self.stake += bet.winAmount()
        return
    
    def lose(self, bet: Bet):
        if isinstance(bet, PrisonOutcome):
            self.stake += bet.amountBet * 0.5
        return