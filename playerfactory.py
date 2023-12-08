#!/usr/bin/env python

from passenger57 import Passenger57
from martingale import Martingale
from sevenreds import SevenReds
from table import Table
from playerrandom import PlayerRandom
from player1326 import Player1326
from playercancellation import PlayerCancellation
from playerfibonacci import PlayerFibonacci

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
        elif self.name.lower() == "playerrandom":
            return PlayerRandom(self.table)
        elif self.name.lower() == "player1326":
            return Player1326(self.table)
        elif self.name.lower() == "playercancel":
            return PlayerCancellation(self.table)
        elif self.name.lower() == "playerfibo":
            return PlayerFibonacci(self.table)
        else:
            raise ValueError