# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:04:55 2019

@author: Sangani
"""

def extract_minutes (str_time):
    h,m = str_time.split(":")
    return int(m)

seq = 'ATGCTGATCagtc'
def sequence (seq):
    seq = seq.upper()
    
    sDNA = {'A','T','G','C'}
    sRNA = {'A','U', 'G','C'}
    
    if sDNA.intersection(seq) == set(seq):
        if {'A','G','C'}.intersection(seq) == set(seq):
            return 'Could  be both'
        else:
            return 'DNA'
    elif sRNA.intersection(seq) == set(seq):
        return 'RNA'
    else:
        return 'Not Valid'

def words(string):
    string = string.split()
    lstring = len(string)
    index = lstring - 1
    
    while index >= 0:
        if len(string[index]) > 3:
            list.append(string[index])
            index = index - 1
        else:
            index = index - 1 
    return list

'''
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    elif line == 'done':
        break
    print (line)
print ('Done!')
'''

num = input('Input series of numbers: ')
order = []
if num.isnumeric():
    num = int(num)
print(num)
for i in num:
    if i not in order:
        order.append(i)
        
order.insert(3,100)
del order[4]

for string in order:
    if order
    
if 3 in order:
   print ('3 is in the list')
print(order)

 

print(order)

for i in list:
    new_list = []
    len(len
    if i > new_list:
        i.append(new_list)
print(new_list)



numbers = input('Please enter random numbers(seperated by commas): ')
def random(numbers):
    number = numbers.split(',')
    for i in number:
        list = []
        if i > 10:
            i.append(list)
        print (list)
            
    

n = int(input('Enter numeric length: '))





