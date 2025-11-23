#!/usr/bin/env python3

from string1 import donuts, both_ends, fix_start, mix_up
from string2 import verbing,not_bad,front_back
from lista1 import match_ends,front_x

def test_donuts():
    assert donuts(4) == 'Fánkok száma: 4'
    assert donuts(9) ==  'Fánkok száma: 9'
    assert donuts(10) ==  'Fánkok száma: sok'
    assert donuts(99) ==  'Fánkok száma: sok'

def test_both_ends():
    assert both_ends('spring') == 'spng'
    assert both_ends('Hello') == 'Helo'
    assert both_ends('a') == ''
    assert both_ends('xyz') == 'xyyz'

def test_fix_start():
    assert fix_start('babble') == 'ba**le'
    assert fix_start('aardvark') == 'a*rdv*rk'
    assert fix_start('google') == 'goo*le'
    assert fix_start('donut') == 'donut'

def test_mix_up():
    assert mix_up('mix', 'pod') == 'pox mid'
    assert mix_up('dog', 'dinner') == 'dig donner'
    assert mix_up('gnash', 'sport') == 'spash gnort'
    assert mix_up('pezzy', 'firm') == 'fizzy perm'

def test_verbing():
    assert verbing('hail') == 'hailing'
    assert verbing('swiming') == 'swimingly'
    assert verbing('do') == 'do'

def test_not_bad():
    assert not_bad('This movie is not so bad') == 'This movie is good'
    assert not_bad('This dinner is not that bad!') == 'This dinner is good!'
    assert not_bad('This tea is not hot') == 'This tea is not hot'
    assert not_bad("It's bad yet not") == "It's bad yet not"

def test_front_back():
    assert front_back('abcd', 'xy') == 'abxcdy'
    assert front_back('abcde', 'xyz') == 'abcxydez'
    assert front_back('Kitten', 'Donut') == 'KitDontenut'

def test_match_ends():
    assert match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']) == 3
    assert match_ends(['', 'x', 'xy', 'xyx', 'xx']) == 2
    assert match_ends(['aaa', 'be', 'abc', 'hello']) == 1

def test_front_x():
    assert front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']) == ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    assert front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']) == ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    assert front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']) == ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']

