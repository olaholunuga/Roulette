#!/usr/bin/env python


from bin_builder import BinBuilder
from game import Game
from simulator import Simulator
from table import Table
from wheel import Wheel
from playerfactory import PlayerFactory
from integerstat import IntegerStatistics


if __name__ == "__main__":
    wheel = Wheel()
    table = Table(wheel, 1000, 1)
    bb = BinBuilder()
    bb.buildBins(wheel)
    player = PlayerFactory("playerfibo", table)
    game = Game(wheel, table)
    sim = Simulator(player, game)
    sim.gather()
    li_maxima = IntegerStatistics(sim.maxima)
    li_duration = IntegerStatistics(sim.durations)
    print(
    """
    MAXIMA STAT:
    MAXIMA MEAN = {}
    MAXIMA STDEV = {}
    
    
    DURATION STAT:
    DURATION MEAN = {}
    DURATION STDEV = {}
    """.format(li_maxima.mean(),
               li_maxima.stdev(),
               li_duration.mean(),
               li_duration.stdev())
    )