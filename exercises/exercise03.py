# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:56:34 2019

@author: Asım

Exercise :

Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""

a , b = 1, 1
liste = []
for i in range(1,12):
    liste.append(a)
    a , b = b , a+b
print(liste)
