#!/usr/bin/env python
from table import Table
from bet import Bet
from player import Player

class Passenger57(Player):
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.black = table.wheel.getOutcome("BLACK")
        # self.won = None
        
    def placeBet(self) -> None:
        """
        Return: 
            None
        """
        amount = 10
        self.stake -= amount
        print(self.stake)
        self.table.placeBet(Bet(amount, self.black))
    
    def Playing(self):
        return True