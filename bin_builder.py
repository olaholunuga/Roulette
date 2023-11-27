#!/usr/bin/env python
from wheel import Wheel
from outcome import Outcome, PrisonOutcome

class BinBuilder:
    """
    """
    
    def buildBins(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel): 
        """
        self.straightBetGen(wheel)
        self.splitBetGen(wheel)
        self.streetBetGen(wheel)
        self.cornerBetGen(wheel)
        self.lineBetGen(wheel)
        self.dozenBetGen(wheel)
        self.columnBetGen(wheel)
        self.evenMoneyBetGen(wheel)
        self.fiveBetGen(wheel)
    
    def straightBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        for i in range(1, 37):
            oc = Outcome(f"Straight {i}", 35)
            wheel.addOutcome(i, oc)
            
        oc1 = Outcome("Zero", 35)
        oc2 = Outcome("Double zero", 35)
        
        wheel.addOutcome(0, oc1)
        wheel.addOutcome(37, oc2)
    
    def splitBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel): 
        """
        for i in range(1, 3):
            for j in range(i, 34 + i, 3):
                oc = Outcome(f"Split {j}-{j + 1}", 17)
                wheel.addOutcome(j, oc)
                wheel.addOutcome(j + 1, oc)
                
        for i in range(1, 4):
            for j in range(i, 31 + i, 3):
                oc = Outcome(f"Split {j}-{j + 3}", 17)
                wheel.addOutcome(j, oc)
                wheel.addOutcome(j + 3, oc)
                
    def streetBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        for i in range(1, 35, 3):
            oc = Outcome(f"Street {i}-{i + 1}-{i + 2}", 11)
            wheel.addOutcome(i, oc)
            wheel.addOutcome(i + 1, oc)
            wheel.addOutcome(i + 2, oc)
    
    def cornerBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (wheel): 
        """
        for i in range(1, 3):
            for j in range(i, 31 + i, 3):
                oc = Outcome(f"Corner {j}-{j + 1}-{j + 3}-{j + 4}", 8)
                for k in [0, 1, 3, 4]:
                    wheel.addOutcome(j + k, oc)
    
    def lineBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        for j in range(1, 32, 3):
                oc = Outcome(f"Line {j}-{j + 1}-{j + 2}-{j + 3}-{j + 4}-{j + 5}", 5)
                for k in range(0, 6):
                    wheel.addOutcome(j + k, oc)
    
    def dozenBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        for i in range(0, 3):
            rang = 12 * (i + 1)
            oc = Outcome(f"Dozen {rang - 11}-{rang}", 2)
            for j in range(0, 12):
                wheel.addOutcome((12 * i) + j + 1, oc)
                
    def columnBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        for i in range(0, 3):
            oc = Outcome(f"Column {i + 1}", 2)
            for j in range(0, 12):
                wheel.addOutcome((3 * j) + i + 1, oc)
    
    def evenMoneyBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        red_oc = Outcome("RED", 1)
        black_oc = Outcome("BLACK", 1)
        even_oc = Outcome("EVEN", 1)
        odd_oc = Outcome("ODD", 1)
        high_oc = Outcome("HIGH", 1)
        low_oc = Outcome("LOW", 1)
        for i in range(1, 37):
            if i > 19:
                wheel.addOutcome(i, low_oc)
            else:
                wheel.addOutcome(i, high_oc)
            if i % 2 == 0:
                wheel.addOutcome(i, even_oc)
            else:
                wheel.addOutcome(i, odd_oc)
            if i in {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}:
                wheel.addOutcome(i, red_oc)
            else:
                wheel.addOutcome(i, black_oc)
    
    def fiveBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        oc = Outcome("FIVE BET", 6)
        for i in [0, 37, 1, 2, 3]:
            wheel.addOutcome(i, oc)

class EuroBinBuilder(BinBuilder):
    """A SubClass of the BinBuilder Class

    Args:
        BinBuilder (_type_):
    """
    
    def buildBins(self, wheel: Wheel) -> None:
        self.fourBetGen(wheel)
        return super().buildBins(wheel)
    
    def straightBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        for i in range(1, 37):
            oc = Outcome(f"Straight {i}", 35)
            wheel.addOutcome(i, oc)
            
        oc1 = PrisonOutcome("Zero", 35)
        oc2 = Outcome("Double zero", 35)
        
        wheel.addOutcome(0, oc1)
        wheel.addOutcome(37, oc2)
    def fiveBetGen(self, wheel: Wheel) -> None:
        """UnImplimented

        Args:
            wheel (Wheel): _description_
        """
        pass
    
    def fourBetGen(self, wheel: Wheel) -> None:
        """

        Args:
            wheel (Wheel):
        """
        oc = Outcome("0-1-2-3", 6)
        for i in [0, 1, 2, 3]:
            wheel.addOutcome(i, oc)