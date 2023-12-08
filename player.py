#!/usr/bin/env python
from table import Table
from bet import Bet
from outcome import PrisonOutcome, Outcome

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
        return False
        
    
    def placeBet(self):
        raise NotImplementedError
    
    def win(self, bet: Bet):
        self.__stake += bet.winAmount()
        self.stat[0] += 1
    
    def lose(self, bet: Bet):
        if isinstance(bet, PrisonOutcome):
            self.stake += bet.amountBet * 0.5
        self.stat[1] += 1
    
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
    
    # def winners(self, outcomes: set[Outcome]) -> None:
    #     """_summary_

    #     Args:
    #         set (Outcome)): _description_
    #     """
    #     if Outcome("RED", 1) in outcomes:
    #         self.redCounts -= 1
    #         print(self.redCounts)