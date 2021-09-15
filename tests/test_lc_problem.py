from src.lc_problems import add

def test_add_pass():
    assert add(1) == 2

def test_add_fail():
    assert add(5) == 6