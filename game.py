#!/usr/bin/env python
from wheel import Wheel
from passenger57 import Passenger57
from table import Table
from dataclasses import dataclass
from passenger57 import Passenger57
from bin_builder import BinBuilder


@dataclass
class Game:
    """
    """
    wheel: Wheel
    table: Table
        
    def cycle(self, player: Passenger57):
        """

        Args:
            player (Passenger57):
        """
        player.placeBet()
        win_bin = self.wheel.choose()
        for bet in iter(self.table):
            if bet.outcome in win_bin:
                player.win(bet)
                print(win_bin)
            else:
                player.lose(bet)
                print(win_bin)


if __name__ == "__main__":
    wheel = Wheel(10)
    table = Table(wheel, 100, 10)
    bb = BinBuilder()
    bb.buildBins(wheel)
    player = Passenger57(wheel, table)
    game_start = Game(wheel, table)
    game_start.cycle(player)
    game_start.cycle(player)
    game_start.cycle(player)