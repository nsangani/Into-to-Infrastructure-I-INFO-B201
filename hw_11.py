# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:35:54 2019

@author: Sangani
"""

file = input('Enter the file name: ')

##Question 1

file_open = open(file)
log = {}
email = []
for i in file_open:
    i = i.rstrip()
    if not i.startswith('From:'):
        if i.startswith('From'):
            i = i.split()
            email.append(i[2])

for name in email:
    log[name] = log.get(name,0) + 1 
print(log)

     
##Question 2

file_open1 = open(file)
logs = {}
emails = []
for ii in file_open1:
    ii = ii.rstrip()
    if not ii.startswith('From:'):
        if ii.startswith('From'):
            ii = ii.split()
            emails.append(ii[1])

for names in emails:
    logs[names] = logs.get(names,0) + 1 
print(logs)       
        