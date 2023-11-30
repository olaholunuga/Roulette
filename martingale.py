#!/usr/bin/env python

from table import Table, InvalidBet
from player import Player
from bet import Bet

class Martingale(Player):
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.lossCount: int = 0
        self.betMultiple: int = 2 ** self.lossCount
        self.black = self.table.wheel.getOutcome("BLACK")
    
    def placeBet(self):
        amount = self.betMultiple
        if amount > self.stake:
            amount = self.stake
        if amount > self.table.limit:
            amount = self.table.limit
        self.stake -= amount
        bet = Bet(amount, self.black)
        try:
            self.table.placeBet(bet)
        except InvalidBet:
            pass
    
    def win(self, bet):
        """

        Args:
            bet (_type_): _description_
        """
        self.lossCount = 0
        self.betMultiple = 2 ** self.lossCount
        return super().win(bet)
    
    def lose(self, bet):
        """

        Args:
            bet (_type_): _description_
        """
        self.lossCount += 1
        self.betMultiple = 2 ** self.lossCount
        return super().lose(bet)