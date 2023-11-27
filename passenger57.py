#!/usr/bin/env python
from table import Table
from wheel import Wheel
from bet import Bet
from outcome import Outcome
from player import Player

class Passenger57(Player):
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.black = table.wheel.getOutcome("BLACK")
        self.won = None
        
    def placeBet(self) -> None:
        """
        Return: 
            None
        """
        self.table.placeBet(Bet(10, self.black))
    
    def Playing(self):
        return True
    
    def win(self, bet: Bet) -> None:
        """

        Args:
            bet (Bet):
        """
        self.won = True
        print(f"Won {bet}")
        return bet.winAmount
    
    def lose(self, bet: Bet) -> None:
        """

        Args:
            bet (Bet): _description_
        """
        self.won = False
        print(f"lost {bet}")