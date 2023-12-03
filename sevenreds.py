#!/usr/bin/env python
from table import Table
from martingale import Martingale
from outcome import Outcome
from typing import Set

class SevenReds(Martingale):
    """

    Args:
        Player (_type_):
    """
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.redCounts = 7
    
    def placeBet(self):
        if self.redCounts == 0:
            return super().placeBet()
    
    def winners(self, outcomes: set[Outcome]) -> None:
        """_summary_

        Args:
            set (Outcome)): _description_
        """
        if Outcome("RED", 1) in outcomes:
            self.redCounts -= 1
            #print(self.redCounts)
        else:
            self.redCounts = 7