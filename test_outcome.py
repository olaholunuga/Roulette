from outcome import Outcome

def test_outcome():
    o1 = Outcome("Red", 1)
    o2 = Outcome("Red", 1)
    o3 = Outcome("Black", 2)
    o4 = Outcome("Black", 1)
    print(o1)
    print(repr(o2))
    assert str(o1) == "Red 1:1"
    assert repr(o2) == "Outcome(name='Red', odds=1)"
    assert o1 == o2
    assert o1.odds == 1
    assert o1.name == "Red"
    assert o1 != o3
    assert o2 != o3
    assert hash(o1) == hash(o2)
    # assert o4 == o3
    
test_outcome()