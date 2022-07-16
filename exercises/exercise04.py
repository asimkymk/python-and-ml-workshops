# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:02:55 2019

@author: Asım
Exercise:

Create a program that asks the user for a number and then prints out a list 
of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly into 
another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

divisorList = []
number = int(input("Please enter your number for find all divisor : "))

for i in range(1,number+1):
    if number % i == 0:
        divisorList.append(i)
print(divisorList)