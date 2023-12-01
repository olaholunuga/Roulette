#!/usr/bin/env python
from table import Table
from bet import Bet
from outcome import PrisonOutcome

class Player:
    
    def __init__(self, table: Table) -> None:
        self.table = table
        self.__stake: int = 0
        self.wheel = self.table.wheel
        self.__roundsToGo: int = 20
        self.stat = [0, 0]
    
    def playing(self):
        if self.__roundsToGo <= 0 or self.stake <= 0:
            return False
        if self.__roundsToGo > 0 or self.stake > 0:
            return True
        False
        
    
    def placeBet(self):
        pass
    
    def win(self, bet: Bet):
        self.__stake += bet.winAmount()
        self.stat[0] += 1
        return
    
    def lose(self, bet: Bet):
        if isinstance(bet, PrisonOutcome):
            self.stake += bet.amountBet * 0.5
        self.stat[1] += 1
        return
    
    @property
    def stake(self):
        return self.__stake
    
    @stake.setter
    def stake(self, amount: int) -> None:
        self.__stake = amount
    
    @property
    def rounds(self):
        return self.__roundsToGo
    
    @rounds.setter
    def rounds(self, num: int) -> None:
        self.__roundsToGo = num
    
    