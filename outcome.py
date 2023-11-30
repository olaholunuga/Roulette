#!/usr/bin/env python
from dataclasses import dataclass

@dataclass(frozen=True)
class Outcome:
    """_summary_
    """
    name: str
    odds: int
    
    def winAmount(self, amount: float) -> float:
        """_summary_

        Args:
            amount (float): _description_

        Returns:
            float: _description_
        """
        return (self.odds * amount) + amount
    
    def __str__(self) -> str:
        """_summary_

        Returns:
            str: _description_
        """
        return f"{self.name:s} {self.odds}:1"

class PrisonOutcome(Outcome):
    """A Subclass of the outcome class

    Args:
        Outcome (_type_): _description_
    """