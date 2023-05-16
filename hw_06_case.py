# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:04:46 2019

@author: Sangani
"""

def case(string):
    """
    Takes a string input and gives the format of only alphabetical string,
    whether it is uppercase, lowercase, mixed, no alphabet, or empty.
    str -> str
    Example: case(ABC) -> uppercase
    """
    if string.isupper():
        return 'upper'
    elif string.islower():
        return 'lower'
    elif string == "":
        return 'empty'
    elif string.isnumeric():
        return 'no alphabet'
    else:
        return 'mixed' 
        
string = input("Enter a string: ")
print("Your string format: " + case(string))
