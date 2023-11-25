#!/usr/bin/env python
from outcome import Outcome
from wheel import Wheel


def test_wheel_sequence():
    wheel = Wheel()
    wheel.addOutcome(8, Outcome("test", 1))
    wheel.rng.seed(1)
    whl = wheel.choose()
    assert Outcome("test", 1) in whl


test_wheel_sequence()
# class test_wheel:
    
#     def test_wheel: