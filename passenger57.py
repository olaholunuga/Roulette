#!/usr/bin/env python
from table import Table
from wheel import Wheel
from bet import Bet
from outcome import Outcome

class Passenger57:
    
    def __init__(self, wheel: Wheel, table: Table) -> None:
        self.wheel = wheel
        self.table = table
        self.black = Outcome("BLACK", 1)
        self.won = None
        
    def placeBet(self) -> None:
        """
        Return: 
            None
        """
        self.table.placeBet(Bet(10, self.black))
    
    def win(self, bet: Bet) -> None:
        """

        Args:
            bet (Bet):
        """
        self.won = True
        print(f"Won {bet}")
    
    def lose(self, bet: Bet) -> None:
        """

        Args:
            bet (Bet): _description_
        """
        self.won = False
        print(f"lost {bet}")