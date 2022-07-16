# -*- coding: utf-8 -*-
"""
Created on Sat May 11 18:02:22 2019

@author: Asım
"""


#%% isminde a harfi bulunanları çağırdık
import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()
cursor.execute("""Select FirstName,LastName from customers where 
               FirstName like '%a%'
               """)

liste = cursor.fetchall()

for row in liste:
    print("First Name : " + row[0])
    print("Last Name  : " + row[1])
    print("*"*50)
    

#%% a harfiyle başlayanları çağırdık
import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()
cursor.execute("""Select FirstName,LastName from customers where 
               FirstName like 'a%'
               """)

liste = cursor.fetchall()

for row in liste:
    print("First Name : " + row[0])
    print("Last Name  : " + row[1])
    print("*"*50)

#%% ismi a ile bitenler
import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()
cursor.execute("""Select FirstName,LastName from customers where 
               FirstName like '%a'
               """)

liste = cursor.fetchall()

for row in liste:
    print("First Name : " + row[0])
    print("Last Name  : " + row[1])
    print("*"*50)