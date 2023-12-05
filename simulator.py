#!/usr/bin/env python
from game import Game
from martingale import Martingale
from wheel import Wheel
from table import Table
from player import Player
from playerfactory import PlayerFactory
from typing import List
from bin_builder import BinBuilder
from sevenreds import SevenReds


class Simulator:
    
    def __init__(self, player: PlayerFactory, game: Game) -> None:
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
        self.bet_num = 0
    
    def session(self) -> List[int]:
        """

        Returns:
            List[int]:
        """
        player = self.player.player()
        player.rounds = self.initDurations
        player.stake = self.initStake
        
        duration = 0
        stakes = [player.stake]
        while player.playing():
            bet = self.game.cycle(player)
            if not bet:
                self.bet_num += 1
            stakes.append(player.stake)
            duration += 1
        self.durations.append(duration)
        self.maxima.append(max(stakes))
        return stakes, player.stake, self.bet_num
    
    def gather(self) -> None:
        roll = 0
        print("  maxima  duration  player_end_stake      bet")
        for _ in range(self.samples):
            sess = self.session()
            print("{:>7}{:>9}{:>17}{:>20}".format(self.maxima[roll], self.durations[roll], sess[1], str(sess[2])))
            self.bet_num = 0
            roll += 1
            
        
        # print(self.durations, len(self.durations))
        # print(self.maxima, len(self.maxima))