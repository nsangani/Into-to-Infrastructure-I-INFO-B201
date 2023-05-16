# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:35:41 2019

@author: Sangani
"""

#Question #1

list = []
n = int(input('Enter numeric length: '))
print('Enter the numbers with consecutive enter key: ')

for i in range(0,n):
    line = int(input())
    list.append(line)
    
final = [list[0],list[-1]]
print(final)
 
   
    
#Question #2

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = a + b

new_line = []
for i in c:
    if i not in new_line:
        new_line.append(i)
print(new_line)



#Question #3

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [bet for bet in a if bet % 2 == 0]

print(b)

  
#Question #4

list_1 = []
n = int(input('Enter numeric length: '))
print('Enter the numbers with consecutive enter key: ')

for i in range(0,n):
    line = int(input())
    list_1.append(line)

list_2 = []
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print(list_2)
        
      
    