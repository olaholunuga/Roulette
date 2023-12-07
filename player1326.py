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
    
    def currenBet(self) -> Bet:
        """

        Returns:
            Bet: _description_
        """
        raise NotImplementedError
    
    def nextWon(self) -> "Player1326State":
        """

        Returns:
            Player1326State:
        """
        raise NotImplementedError
    
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
    
    def currenBet(self) -> Bet:
        amount = 10
        if amount > self.stake:
            amount = self.stake
        if amount > self.table.limit:
            amount = self.table.limit
        self.player.stake -= amount
        return Bet(10, self.player.outcome)
    
    def nextWon(self) -> Player1326State:
        """

        Returns:
            Player1326State: _description_
        """
        return Player1362OneWin(self.player)
    
class Player1362OneWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
    
    def currenBet(self) -> Bet:
        amount = 10 * 3
        if amount > self.stake:
            amount = self.stake
        if amount > self.table.limit:
            amount = self.table.limit
        self.player.stake -= amount
        return Bet(10 * 3, self.player.outcome)
    
    def nextWon(self) -> Player1326State:
        return Player1362TwoWin(self.player)

class Player1362TwoWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
    
    def currenBet(self) -> Bet:
        amount = 10 * 2
        if amount > self.stake:
            amount = self.stake
        if amount > self.table.limit:
            amount = self.table.limit
        self.player.stake -= amount
        return Bet(10 * 2, self.player.outcome)
    
    def nextWon(self) -> Player1326State:
        return Player1362ThreeWin(self.player)

class Player1362ThreeWin(Player1326State):
    """

    Args:
        Player1326State (Player1362State):
    """
    def __init__(self, player: Player) -> None:
        super().__init__(player)
    
    def currenBet(self) -> Bet:
        amount = 10 * 6
        if amount > self.stake:
            amount = self.stake
        if amount > self.table.limit:
            amount = self.table.limit
        self.player.stake -= amount
        return Bet(10 * 6, self.player.outcome)
    
    def nextWon(self) -> Player1326State:
        return Player1326NoWins(self.player)

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
        self.stake -= bet.amountBet
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