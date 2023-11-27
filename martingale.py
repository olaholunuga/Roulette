from Roulette.table import Table
from player import Player

class martingale(Player):
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)