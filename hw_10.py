# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 15:14:19 2019

@author: Sangani
"""
'''
## Question 1

t = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)

def count(t,x):
    """
    Takes tuples and counts # of x present in tuple t
    tuple -> int
    """
    count = 0
    for i in t:
        if i == x:
            count += 1
            
    return count

y = 4
z = 8

print('Total 4s are: ' + str(count(t,y)))
print('Total 8s are: ' + str(count(t,z)))

'''
## Question 2


value = input("Input numbers between 0 and 5(with no space in between): ")
val = tuple(value)

def convert(val):
    """
    Takes a number and covert into words
    1 -> 'one'
    tuple -> str
    """
    word = ""
    for number in value:
        if number == '0':
            word = str(word) + "zero "
            continue
        if number == '1':
            word = str(word) + 'one '
            continue
        if number == '2':
            word = str(word) + 'two '
            continue
        if number == '3':
            word = str(word) + 'three '
            continue
        if number == '4':
            word = str(word) + 'four '
            continue
        else:
            print('Not between 0 and 5')
    return word

print(convert(value))

'''
## Question 3

data = ((0.001,0.5),( 0.002,0.7),(0.005,0.9),(0.009,0.3),( 0.006,0.1))

print(data[0][1])
print(data[2][0])
print(data[3][0], data[3][1])

## Question 4
    
Tuples = ('P','R','O','G','R','A','M','M','I','N','G')

def TupleToString(Tuples):
    """
    Takes a Tuple and puts them together into a word
    tuple -> str
    """
    return ''.join(Tuples)

print(TupleToString(Tuples))
'''