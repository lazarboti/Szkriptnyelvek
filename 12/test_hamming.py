#!/usr/bin/env python3


from hamming import hamming

def test_hamming():
    assert hamming("roses", "toned") == 3
    assert hamming("abc", "") == -1
    assert hamming("alma", "alma") == 0
    assert hamming("abc", "dfg") == 3