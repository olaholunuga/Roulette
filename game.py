#!/usr/bin/env python
from wheel import Wheel
from passenger57 import Passenger57
from table import Table
from dataclasses import dataclass
from passenger57 import Passenger57
from bin_builder import BinBuilder
from martingale import Martingale


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
        if player.playing():
            player.placeBet()
        win_bin = self.table.wheel.choose()
        player.roundsToGo -= 1
        for bet in iter(self.table):
            if bet.outcome in win_bin:
                player.win(bet)
            else:
                player.lose(bet)
        return win_bin


if __name__ == "__main__":
    wheel = Wheel(10)
    table = Table(wheel, 100, 1)
    bb = BinBuilder()
    bb.buildBins(wheel)
    player = Passenger57(table)
    player2 = Martingale(table)
    player2.stake = 200
    game_start = Game(wheel, table)
    for i in range(4):
        print(game_start.cycle(player2))
        print(player2.stake)