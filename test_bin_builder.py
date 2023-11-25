#!/usr/bin/env python
from bin_builder import BinBuilder
from wheel import Wheel
# from unittest import TestCase

class TestBinBuider():
    """

    Args:
        TestCase (_type_):
    """
    def __init__(self) -> None:
        self.wheel = Wheel(1)
        self.bin_builder = BinBuilder()
        self.bin_builder.buildBins(self.wheel)
        
    def test_five_bet(self):
        for i in [0, 1, 2, 3, 37]:
            wik = self.wheel.get(i)
            print(wik)
            
    def test_corner(self):
        oc_list = []
        for i in range(1, 37):
            wik = self.wheel.get(i)
            for oc in wik:
                if oc.name[:3] == "Cor":
                    if oc not in oc_list:
                        oc_list.append(oc)
        for i, v in enumerate(oc_list):           
            print(i, v)

testBuilder = TestBinBuider()
testBuilder.test_corner()