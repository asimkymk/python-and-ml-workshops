# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:17:51 2019

@author: Asım

Exercise:
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.
"""

name = input("Please enter your name : ")
age = int(input("Hello {}, please enter your age : ".format(name)))
year = 2019
birthYear = year - age
hundredYearOld = birthYear + 100
print("""Dear {}

Your Age : {}

Year That yours 100 years old :  {}

""".format(name,age,hundredYearOld))
