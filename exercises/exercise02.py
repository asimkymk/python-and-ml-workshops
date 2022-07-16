# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:51:23 2019

@author: Asım

Execise : 
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?
"""
number = int(input("Please enter a number : "))

if number % 2 == 0:
    print("{} is a even.".format(number))
else:
    print("{} is a odd.".format(number))
