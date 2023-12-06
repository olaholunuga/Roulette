#!/usr/bin/env python
from table import Table
from bet import Bet
from player import Player

class Passenger57(Player):
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.black = table.wheel.getOutcome("BLACK")
        self.bet = None
        
    def placeBet(self) -> None:
        """
        Return: 
            None
        """
        amount = 10
        self.stake -= amount
        self.bet = Bet(amount, self.black)
        self.table.placeBet(self.bet)
    
    def Playing(self):
        return True
    
    def winners(self, outcomes) -> None:
        pass