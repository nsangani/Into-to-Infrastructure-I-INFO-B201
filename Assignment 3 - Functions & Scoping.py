#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Write a program to ask the user to input a float number and output the rounded 
# value of it using related function. (1 point)


# In[2]:


value = float(input('Enter a float value: '))
print('Rounded value is ' + str(round(value)))


# In[3]:


# Convert the program above to a function that accepts a float and returns 
# the rounded value. Test your function by testing all values between 
# 0 and 1.0 (inclusive) by tenths. (i.e. 0.0, 0.1, 0.2, ...) (1 point)


# In[8]:


def rounded_val(value):
    """Takes float and returns rounded values"""
    return ('Rounded value is ' + str(round(value))) 

for i in [x * 0.1 for x in range(0, 11)]:  # If Inclusive then why not phrase it 0 to 1?
    print(i, " => " + rounded_val(i))


# In[5]:


# Write a function to calculate the square root of the provided parameter 
# using the Newton-Raphson method. Print the difference between the square 
# of the calculated value and the result of request. (4 points)


# In[15]:


def Newton_Raphson_sr(k,epsilon = 0.01):
    """ Find x such that x**2 - k is within epsilon = 0.01 as default """
    guess = k/2.0
    number_guesses = 1
    while abs(guess*guess - k) >= epsilon:
        guess = guess - (((guess**2) - k)/(2*guess))
        number_guesses += 1
    return guess

import math

# Not sure what 'provided parameter' means so used the range parameter 0 to 1 from previous question 
# Also not sure what 'the difference between the square of the calculated value and the result of request' mean so..
# I'm assuming it is expected vs Newton Raphson calculated sqrt value
# Hope this calculation suffice the general idea of the question

print('Expected_value vs Newton_Raphson_square_root_value')
for i in [x * 0.1 for x in range(0, 11)]:
    print(i, " => " +str(math.sqrt(i)), "vs " + str(Newton_Raphson_sr(i)))


# In[6]:


# Write a function called 'area' that accepts 2 required parameters and 1 optional
# parameters. Assume all are numeric. If only 2 parameters are provided the function
# calculates the area of a rectangle and if all 3 are provided it will return 
# the surface area of the cuboid with those dimensions. (2 points)


# In[27]:


def area(length, width, height=None):
    """
    Input first two parameters to calculate the area (l+w). 
    Ex. area(1,2) => 2
    Input all three parameters to calulate the surface area of the cuboid is calulated (l+w+h).
    Ex. area(1,2,3) => 6
    """
    if height != None:
        SA_of_cuboid = length + width + height
        x = SA_of_cuboid
    else:
        area_of_rec = length * width
        x = area_of_rec
    return x

l = 1
w = 2
h = 3
print('Length =', l, ', Width =', w, ', Height =', h)
print('Area of the rectangle: '+ str(area(l,w)))
print('Surface area of the cuboid: '+ str(area(l,w,h)))
    

