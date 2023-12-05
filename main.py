#!/usr/bin/env python


from bin_builder import BinBuilder
from game import Game
from simulator import Simulator
from table import Table
from wheel import Wheel
from playerfactory import PlayerFactory


if __name__ == "__main__":
    wheel = Wheel()
    table = Table(wheel, 1000, 1)
    bb = BinBuilder()
    bb.buildBins(wheel)
    player = PlayerFactory("passenger57", table)
    game = Game(wheel, table)
    sim = Simulator(player, game)
    sim.gather()