#!/usr/bin/env python
from table import Table, InvalidBet
from pytest import raises
from outcome import Outcome
from bet import Bet
from wheel import Wheel
from unittest import TestCase

class TestTable(TestCase):
    
    def setUp(self):
        wheel = Wheel()
        self.table = Table(wheel, 100, 10)
        
    def test_placebet(self):
        
        with raises(InvalidBet):
            self.table.placeBet(Bet(9, Outcome("1", 35)))
        
        assert Bet(9, Outcome("1", 35)) in self.table.bets
        
        with raises(InvalidBet):
            self.table.placeBet(Bet(100, Outcome("0", 35)))
            
    def test_repr(self):
        
        rep = self.table.__repr__()
        assert isinstance(rep, str)
        
    def test_str(self):
        self.table.placeBet(Bet(60, Outcome("7", 35)))
        strr = self.table.__str__()
        assert isinstance(strr, str)
        
    def test_table(self):
        bet = Bet(11, Outcome("1", 35))
        self.table.placeBet(bet)
        self.assertIn(bet, self.table.bets)