# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:00:42 2019

@author: Asım
"""

class Insan:
    def __init__(self,firstname, secondname, Age):
        self.firstname = firstname
        self.secondname = secondname
        self.age = Age
        
insan1 = Insan("Asım","Kaymak",18)
print(insan1.firstname)
print(insan1.secondname)
print(insan1.age)


class Worker(Insan):
    def __init__(self,salary):
        self.salary = salary
        
class Customer(Insan):
    def __init__(self, creditcardnumber):
        self.credit = creditcardnumber
    
ahmet = Worker(1900)