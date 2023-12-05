#!/usr/bin/env python

from passenger57 import Passenger57
from martingale import Martingale
from sevenreds import SevenReds
from table import Table

class PlayerFactory:
    """A Player initializer for the User of the Subclasses of Player to choose any player of their choice
    """
    
    def __init__(self, player_name: str, table: Table) -> None:
        self.name = player_name
        self.table = table
    def player(self) -> ( Passenger57 | Martingale | SevenReds ):
        """ return the player who's name is passed
        """
        if self.name.lower() == "passenger57":
            return Passenger57(self.table)
        elif self.name.lower() == "martingale":
            return Martingale(self.table)
        elif self.name.lower() == "sevenreds":
            return SevenReds(self.table)
        else:
            raise ValueError