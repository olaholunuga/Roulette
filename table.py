#!/usr/bin/env python
from typing import Iterator
from bet import Bet
from wheel import Wheel

class InvalidBet(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Table:
    
    def __init__(self, *bets: list[Bet]) -> None:
        """

        Args:
            bets (Bet): _description_
        """
        self.limit: int = None
        self.minimum: int = None
        self.bets: list[Bet] = bets
        
    def placeBet(self, bet: Bet) -> None:
        """

        Args:
            bet (Bet): _description_
        """
        try:
            if self.limit and bet > self.limit:
                raise InvalidBet
            if self.minimum and bet < self.minimum:
                raise InvalidBet
        except InvalidBet as err:
            pass
        self.bets.append(bet)
    
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
        return f"Table {self.bets}"
    
    def isValid(self):
        for b in self.bets:
            if b.amountBet > self.limit or b.amountBet < self.minimum:
                raise InvalidBet