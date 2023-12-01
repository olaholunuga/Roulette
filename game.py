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
        
    def cycle(self, player: Martingale):
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
        return player.bet


if __name__ == "__main__":
    wheel = Wheel()
    table = Table(wheel, 100, 1)
    bb = BinBuilder()
    bb.buildBins(wheel)
    player = Passenger57(table)
    player2 = Martingale(table)
    player2.stake = 100
    game_start = Game(wheel, table)
    print(f"Stake before games: {player2.stake}")
    while player2.playing():
        game_start.cycle(player2)
    print(f"WINS - {player2.stat[0]}\nLOSE - {player2.stat[1]}")
    print(f"Stake After games: {player2.stake}")