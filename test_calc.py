import calc    # The code to test

def test_increment():
    assert calc.increment(3) == 4

def test_decrement():
    assert calc.decrement(3) == 2

#python -m pytest