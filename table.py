#!/usr/bin/env python
from typing import Iterator
from bet import Bet
from wheel import Wheel
from pprint import saferepr

class InvalidBet(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Table:
    
    def __init__(self, wheel, limit, minimum) -> None:
        """

        Args:
            bets (Bet): _description_
        """
        self.wheel: Wheel = wheel
        self.limit: int = limit
        self.minimum: int = minimum
        self.bets: list[Bet] = []
        
    def placeBet(self, bet: Bet) -> None:
        """

        Args:
            bet (Bet): _description_
        """
        self.bets.append(bet)
        if not self.isValid():
            raise InvalidBet
        
    
    def __iter__(self) -> Iterator[Bet]:
        """
        Yields:
            Iterator[Bet]: _description_
        """
        for b in self.bets:
            yield b
    
    def __str__(self) -> str:
        """

        Returns:
            str: _description_
        """
        return saferepr(self.bets)
    
    def __repr__(self) -> str:
        """

        Returns:
            str:
        """
        return "Table({})".format("".join((str(x) for x in self.bets)))
    
    def isValid(self) -> bool:
        """

        Returns:
            bool:
        """
        bet_sum = sum(x.amountBet for x in self.bets)
        if bet_sum > self.limit:
            return False
        return True
    
    def bets_clear(self) -> None:
        self.bets.clear()