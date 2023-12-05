#!/usr/bin/env python
from table import Table
from bet import Bet
from player import Player

class Passenger57(Player):
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.black = table.wheel.getOutcome("BLACK")
        # self.won = None
        self.bet = None
        
    def placeBet(self) -> None:
        """
        Return: 
            None
        """
        amount = 10
        self.stake -= amount
        # print(self.stake)
        self.bet = Bet(amount, self.black)
        self.table.placeBet(self.bet)
    
    def Playing(self):
        return True
    
    def winners(self, outcomes) -> None:
        """_summary_

        Args:
            set (Outcome)): _description_
        # """
        # if Outcome("RED", 1) in outcomes:
        #     self.redCounts -= 1
        #     #print(self.redCounts)
        # else:
        #     self.redCounts = 7