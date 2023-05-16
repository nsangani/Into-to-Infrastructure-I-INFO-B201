# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:33:43 2019

@author: Sangani
"""

'''
import os
os.getcwd()
'''

## Question 1

gg = input("Enter the file name: ")

bet = open(gg)


for line in bet:
    print (line.upper())



## Question 2
  
ok = input("Enter the file name: ")  

wallah = open (ok)

only = 1

for linea in wallah:
    if only % 2 == 0:
        print(linea)
    only = only + 1
    
## Question 3
    
fun = input("Enter the file name: ")
ll = open(fun)

ok = []

for ruler in ll:
    ruler = ruler.rstrip()
    r = ruler.split(" ")
    for words in r:
        if words not in ok:
            ok.append(words)
ok.sort()
print (ok)

    