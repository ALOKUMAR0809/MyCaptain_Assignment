# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:47:15 2022

@author: Alok Kumar
"""

# print positive Numbers in a Range
  
# input of list
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)

print("Positive numbers in",li,"are: ")
  
#traversing
for i in li:   
    # checking condition
    if i >= 0:
       print(i, end = " ")