# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:03:49 2019

@author: Sangani
"""


count = 0
total = 0
Avg = 0
number = input('Enter a number: ')

while True:
    line = input(number)
    try:
        line = float(line)
        count = count + 1
        total = total + line
        avg = total/count  
    except:
        if line == 'done':
            break
        else:
            print("Bad Data")
            continue
    
print(count, total, avg)


count = 0
max = 0
min = 0

number = input('Enter a number: ')
 
while True:
    line = input(number)
    line = float(line)
    count = count + line
    if number>max:            #IDK how to fix this 
        max = number
    elif number<min:
        min = number
    elif line == 'done':
        break
    else:
        print("Bad Data")
        continue
         
print(max, min)

        
    
'''
for line in value:
     sum = line + sum
     print (sum)
'''  

