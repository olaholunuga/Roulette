#!/usr/bin/env python
from wheel import Wheel
from passenger57 import Passenger57
from table import Table
from dataclasses import dataclass
from passenger57 import Passenger57
from bin_builder import BinBuilder
from martingale import Martingale
from sevenreds import SevenReds
from player1326 import Player1326

@dataclass
class Game:
    """
    """
    wheel: Wheel
    table: Table
        
    def cycle(self, player: ( SevenReds | Martingale | Passenger57 | Player1326 )):
        """

        Args:
            player (Passenger57):
        """
        self.table.bets_clear()
        if player.playing():
            player.placeBet()
        win_bin = self.table.wheel.choose()
        player.rounds -= 1
        for bet in iter(self.table):
            if bet.outcome in win_bin:
                player.win(bet)
            else:
                player.lose(bet)
        if player.__class__ == (SevenReds | Martingale):
            player.winners(set(win_bin))