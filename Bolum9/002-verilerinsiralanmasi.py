# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:26:22 2019

@author: Asım
"""

import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("""Select FirstName, LastName, City from customers 
               where city = 'Berlin' or city = 'Prague'
               order by FirstName,LastName""") # isme göre sıralıyoruz 
#ismi aynı olanlar soyadlarına göre sıralanıyor
liste = cursor.fetchall()
for row in liste:
    print("First Name : " + row[0])
    print("Last Name  : " + row[1])
    print("Ciy        : " + row[2])
    print("*"*50)
connection.close()