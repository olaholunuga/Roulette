#!/usr/bin/env python
from os import urandom
from outcome import Outcome
from bin import Bin
from typing import Iterator
from random import Random, randint

class Wheel:
    
    def __init__(self, seed=None) -> None:
        self.bins = tuple(Bin([]) for i in range(38))
        self.rng = Random()
        self.all_outcomes = dict()
        if seed:
            self.rng.seed(seed)
        else:
            self.rng.seed(urandom(8))
        self.choice = None
        
    def addOutcome(self, number: int, outcome: Outcome) -> None:
        """_summary_

        Args:
            number (int): _description_
            outcome (Outcome): _description_
        """
        if outcome not in self.all_outcomes:
            self.all_outcomes[outcome.name] = outcome
        bin_list = list(self.bins)
        oc_bin = set(bin_list[number].copy())
        if outcome not in oc_bin:
            oc_bin.add(outcome)
        bin_list[number] = Bin(oc_bin)
        
        self.bins = bin_list
        
    def getOutcome(self, name: str) -> Outcome:
        """_summary_

        Args:
            name (str):

        Returns:
            Outcome: 
        """
        return self.all_outcomes[name]
    
    def choose(self) -> Bin:
        """_summary_

        Returns:
            Bin: _description_
        """
        rng = self.rng.randint(0, 37)
        self.choice = self.bins[rng]
        return self.choice
    
    def get(self, bin: int) -> Bin:
        """_summary_

        Args:
            bin (int): _description_

        Returns:
            Bin: _description_
        """
        return self.bins[bin]
    
    def binIterator(self) -> list[Outcome]:
        """_summary_

        Returns:
            lis[Outcome]: list of outcomes
        """
        all_oc = []
        for v in self.all_outcomes.values():
            all_oc.append(v)
        return all_oc