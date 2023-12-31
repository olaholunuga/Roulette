#!/usr/bin/env python
from outcome import Outcome
from dataclasses import dataclass


@dataclass
class Bet:
    """
    """
    amountBet: int
    outcome: Outcome
    
    def winAmount(self) -> int:
        return self.outcome.winAmount(self.amountBet) # self.amountBet * self.outcome.odds
    
    def loseAmount(self) -> int:
        return self.amountBet
        
    def __str__(self) -> str:
        return F"{self.amountBet} on {self.outcome}"