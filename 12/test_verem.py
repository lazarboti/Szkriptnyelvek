from verem import Verem

def test_ures_verem():
    v = Verem()
    assert v.ures() is True
    assert v.meret() == 0
    assert v.kivesz() is None
    assert str(v) == "["

def test_betesz_mukodik():
    v = Verem()
    v.betesz(1)
    v.betesz(4)
    assert v.meret() == 2
    assert not v.ures()
    assert str(v) == "[1 4"

def test_kivesz_mukodik():
    v = Verem()
    v.betesz(1)
    v.betesz(2)
    v.betesz(3)
    x = v.kivesz()
    assert x == 3
    assert v.meret() == 2
    assert str(v) == "[1 2"

def test_kivesz_uresbol():
    v = Verem()
    assert v.kivesz() is None
