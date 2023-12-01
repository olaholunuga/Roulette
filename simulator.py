#!/usr/bin/env python
from game import Game
from martingale import Martingale
from wheel import Wheel
from table import Table
from player import Player
from typing import List
from bin_builder import BinBuilder

class Simulator:
    
    def __init__(self, player: Player, game: Game) -> None:
        """
        Args:
            player (Player): _description_
            game (Game): _description_
        """
        self.initDurations = 250
        self.initStake = 100
        self.samples = 50
        self.durations = []
        self.maxima = []
        self.player = player
        self.game = game
    
    def session(self) -> List[int]:
        """

        Returns:
            List[int]:
        """
        self.player.rounds = self.initDurations
        self.player.stake = self.initStake
        
        duration = 0
        stakes = [self.player.stake]
        while self.player.playing():
            bet = self.game.cycle(self.player)
            stakes.append(self.player.stake)
            duration += 1
        self.durations.append(duration)
        self.maxima.append(max(stakes))
        return stakes, player.stake, bet
    
    def gather(self) -> None:
        roll = 0
        print("maxima    duration    player_end_stake    bet")
        for _ in range(self.samples):
            sess = self.session()
            print("{}   {}    {}    {}".format(self.maxima[roll], self.durations[roll], sess[1], sess[2]))
            roll += 1
            
        
        # print(self.durations, len(self.durations))
        # print(self.maxima, len(self.maxima))


if __name__ == "__main__":
    wheel = Wheel()
    table = Table(wheel, 1000, 1)
    bb = BinBuilder()
    bb.buildBins(wheel)
    player = Martingale(table)
    game = Game(wheel, table)
    sim = Simulator(player, game)
    sim.gather()
    