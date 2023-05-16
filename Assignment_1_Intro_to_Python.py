#!/usr/bin/env python
# coding: utf-8

# In[22]:


# Import Library

import random 


# In[6]:



 n = input('Enter an integer')
print(type(n))


# In[23]:


# Calculate the area of the rectangle with width 5 and length 10.5 and print out the result. (2 points)

width = 5
length = 10.5
Area_of_the_rectangle = width*length
print('Area_of_the_rectangle :', Area_of_the_rectangle)


# In[24]:


# Define a number and print the square value of the number. (2 points)

number = random.randint(0,100)
print('number =', number)
print('number squared =', number**2 )


# In[25]:


# Check the data types of following objects: (total 2 points)
# 9999.34
# informatics
# 57687
# b501

print('9999.34 : ', type(9999.34))
print('informatics : ', type('informatics'))
print('57687 : ', type(57687))
print('b501 :', type('b501'))


# In[26]:


# For the given number 96321, write a python script which prints whether the given number is divisible by 3 or 4 or none. (4 points)

def divisible_of(n):
    if not n % 3:
        return('Divisible by 3')
    if not n % 4:
        return('Divisible by 4')
    else:
        return('none')
         
print(divisible_of(96321))

