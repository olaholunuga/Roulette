from abc import ABCMeta
from outcome import Outcome
from table import Table, InvalidBet
from player import Player
from bet import Bet

class Player1326State(metaclass=ABCMeta):
    """DC

    Args:
        metaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """
    def __init__(self, player: Player) -> None:
        self.player = player
        self.betAmount = 0
        self.nextStateWin = None
    
    def currenBet(self) -> Bet:
        """

        Returns:
            Bet: _description_
        """
        amount = 10 * self.betAmount
        if amount > self.player.stake:
            amount = self.player.stake
        if amount > self.player.table.limit:
            amount = self.player.table.limit
        self.player.stake -= amount
        return Bet(amount, self.player.outcome)
    
    def nextWon(self) -> "Player1326State":
        """

        Returns:
            Player1326State:
        """
        return self.player.states.get(self.nextStateWin) # self.nextStateWin(self.player)
    
    def nextLost(self) -> "Player1326State":
        """

        Returns:
            Player1326State:
        """
        return self.player.states.get("noWin") # Player1326NoWins(self.player)

class Player1326NoWins(Player1326State):
    """

    Args:
        Player1326State (Player1326State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 1
        self.nextStateWin = "oneWin"
    
class Player1362OneWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 3
        self.nextStateWin = "twoWin"

class Player1362TwoWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 2
        self.nextStateWin = "threeWin"

class Player1362ThreeWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 6
        self.nextStateWin = "noWin"

class Player1326StateFactory:
    
    def __init__(self, player: Player) -> None:
        self.values = {
            "noWin": Player1326NoWins(player),
            "oneWin": Player1362OneWin(player),
            "twoWin": Player1362TwoWin(player),
            "threeWin": Player1362ThreeWin(player)
        }
    def get(self, name: str) -> Player1326State:
        """
        Args:
            name (str): _description_

        Returns:
            Player1326State: _description_
        """
        return self.values[name]

class Player1326(Player):
    """

    Args:
        Player (Player):
    """
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = self.table.wheel.getOutcome("BLACK")
        self.states = Player1326StateFactory(self)
        self.state: (Player1326NoWins |
                     Player1362OneWin |
                     Player1362TwoWin |
                     Player1362ThreeWin) = self.states.get("noWin")
    
    def placeBet(self) -> Bet:
        bet = self.state.currenBet()
        try:
            self.table.placeBet(bet)
        except InvalidBet:
            pass
    
    def win(self, bet: Bet) -> None:
        self.state = self.state.nextWon()
        super().win(bet)
    
    def lose(self, bet: Bet) -> None:
        self.state = self.state.nextLost()
        super().lose(bet)