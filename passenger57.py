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
        won = self.table.bets
        print("Won")
    
    def lose(self, bet: Bet) -> None:
        """

        Args:
            bet (Bet): _description_
        """
        print("lost")