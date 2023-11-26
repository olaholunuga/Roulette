#!/usr/bin/env python
from bin_builder import BinBuilder
from wheel import Wheel
from unittest import TestCase
from outcome import Outcome

class TestBinBuider(TestCase):
    """

    Args:
        TestCase (_type_):
    """
    def setUp(self):
        self.wheel = Wheel(1)
        self.bin_builder = BinBuilder()
        self.bin_builder.buildBins(self.wheel)
        
    def test_five_bet(self):
        for i in range(1, 37):
            self.assertIn(Outcome(f"Straight {i}", 35), self.wheel.get(i), F"{i} i not in bins")
        
        self.assertIn(Outcome("Zero", 35), self.wheel.get(0), F"0 not in bins")
        self.assertIn(Outcome("Double zero", 35), self.wheel.get(37), F"37 not in bins")
    
    def test_corner(self):
        for i in range(1, 3):
            for j in range(i, 31 + i, 3):
                oc = Outcome(f"Corner {j}-{j + 1}-{j + 3}-{j + 4}", 8)
                for k in [0, 1, 3, 4]:
                    self.assertIn(oc, self.wheel.get(j + k), F"corner not in bins")