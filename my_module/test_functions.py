"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

import random 
from my_module.functions import *

def test_format_answers():
    
    assert callable(format_answers)
    assert isinstance(format_answers(['A', 'B', 'C', 'D']), list)
    assert format_answers('A') == ['A']
    assert format_answers('a') == ['A']
    assert format_answers('aa') != ['A']

def test_test():
    
    assert callable(test)
    
def test_phoebe_song():
    
    assert callable(phoebe_song)
    assert isinstance(phoebe_song(), str)  

def test_calculate_score(answers_list):
    
    assert callable(calculate_score)
    assert isinstance(calculate_score(answers_list), str) # this is checking the output    



                 
    