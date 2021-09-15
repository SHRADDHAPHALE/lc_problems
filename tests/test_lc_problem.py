from src.lc_problems import add, add2

def test_add_pass():
    assert add(1) == 2

def test_add_fail():
    assert add(5) == 6

def test_add2_pass():
    assert add2(1) == 3

def test_add2_fail():
    assert add2(3) == 5