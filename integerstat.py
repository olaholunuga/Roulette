#!/usr/bin/env python
from math import sqrt

class IntegerStatistics(list):
    """This class is an extension of the python built-in list class
       to calculate the mean and standard deviation of a list of integers

    Args:
        list (list):
    """
    
    def mean(self) -> float:
        """method to calculate the mean of the given list of integers

        Returns:
            float:
        """
        return sum(self)/len(self)
    
    def stdev(self) -> float:
        """method to calculate the statdard deviation of list of integers

        Returns:
            float:
        """
        m = self.mean()
        return sqrt(sum((x-m)**2 for x in self) / (len(self)-1))

# li = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
# li_is = IntegerStatistics(li)
# print(li_is.mean())
# print(li_is.stdev())