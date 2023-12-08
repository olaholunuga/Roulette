#!/usr/bin/env python

from player import Player
from bet import Bet
from table import Table, InvalidBet

class PlayerFibinacci(Player):
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = self.table.wheel.getOutcome("BLACK")
        self.recent = 1
        self.previous = 0
    
    def placeBet(self):
        amount = self.recent
        if amount > self.stake:
            amount = self.stake
        if amount > self.table.limit:
            amount = self.table.limit
        self.stake -= amount
        bet = Bet(amount, self.outcome)
        try:
            self.table.placeBet(bet)
        except InvalidBet:
            print("Invalid bet Error")
    
    def win(self, bet: Bet):
        super().win(bet)
        self.recent = 1
        self.previous = 0
    
    def lose(self, bet: Bet):
        super().lose(bet)
        next = self.previous + self.recent
        self.previous = self.recent
        self.recent = next