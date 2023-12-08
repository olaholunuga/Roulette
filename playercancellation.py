#!/usr/bin/env python
from Roulette.table import Table, InvalidBet
from player import Player
from bet import Bet

class PlayerCancellation(Player):
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = self.table.wheel.getOutcome("BLACK")
        self.sequence = None
        self.resetSequence()
    
    def resetSequence(self) -> None:
        self.sequence = [1, 1, 1, 1, 1, 1]
    
    def placeBet(self):
        amount = self.sequence[0] + self.sequence[-1]
        if amount > self.stake:
            amount = self.stake
        if amount > self.table.limit:
            amount = self.table.limit
        self.stake -= amount
        bet = Bet(amount, self.outcome)
        try:
            self.table.placeBet(bet)
        except InvalidBet:
            pass
    
    def win(self, bet: Bet):
        super().win(bet)
        del self.sequence[-1]
        del self.sequence[0]
    
    def lose(self, bet: Bet):
        super().lose(bet)
        f_l_sum = self.sequence[0] + self.sequence[-1]
        self.sequence.append(f_l_sum)