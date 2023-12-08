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
        return self.nextStateWin(self.player)
    
    def nextLost(self) -> "Player1326State":
        """

        Returns:
            Player1326State:
        """
        return Player1326NoWins(self.player)

class Player1326NoWins(Player1326State):
    """

    Args:
        Player1326State (Player1326State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 1
        self.nextStateWin = Player1362OneWin
    
class Player1362OneWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 3
        self.nextStateWin = Player1362TwoWin

class Player1362TwoWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 2
        self.nextStateWin = Player1362ThreeWin

class Player1362ThreeWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
        self.betAmount = 6
        self.nextStateWin = Player1326NoWins



class Player1326(Player):
    """

    Args:
        Player (Player):
    """
    
    def __init__(self, table: Table) -> None:
        super().__init__(table)
        self.outcome = self.table.wheel.getOutcome("BLACK")
        self.state: (Player1326NoWins |
                     Player1362OneWin |
                     Player1362TwoWin |
                     Player1362ThreeWin) = Player1326NoWins(self)
    
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