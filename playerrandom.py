#!/usr/bin/env python
from bet import Bet
from table import InvalidBet, Table
from player import Player
from random import Random, choice
from wheel import Wheel

class PlayerRandom(Player):
    """A subclass of Player class

    Args:
        Player (_type_): _description_
    """
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.rng = Random()
    
    def placeBet(self):
        amount = 10
        if amount > self.stake:
            amount = self.stake
        if amount > self.table.limit:
            amount = self.table.limit
        self.stake -= amount
        all_oc = self.table.wheel.binIterator()
        oc = choice(all_oc)
        print(oc, self.stake)
        self.bet = Bet(amount, oc)
        try:
            self.table.placeBet(self.bet)
        except InvalidBet:
            print("Invalid bet Error")