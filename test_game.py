#!/usr/bin/env python
from bin_builder import BinBuilder
from game import Game
from table import Table
from wheel import Wheel
from passenger57 import Passenger57
from unittest import TestCase

class TestGame(TestCase):
    
    def setUp(self) -> None:
        self.wheel = Wheel(10)
        self.table = Table(self.wheel, 100, 10)
        bb = BinBuilder()
        bb.buildBins(self.wheel)
        self.player = Passenger57(self.wheel, self.table)
        game_start = Game(self.wheel, self.table)
        game_start.cycle(self.player)
    
    def test_cycle(self):
        if self.player.won:
            assert self.player.black in [bin.outcome for bin in self.table]
            assert self.player.black in self.wheel.choice
        else:
            assert self.player.black in [bin.outcome for bin in self.table]
            assert self.player.black not in self.wheel.choice