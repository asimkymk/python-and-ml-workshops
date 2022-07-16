# -*- coding: utf-8 -*-
"""
Created on Sat May 11 14:41:35 2019

@author: Asım



"""

#%%
import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.execute("Select FirstName, LastName from customers")

for row in cursor:
    print("First Name = " + row[0])
    print("Last Name = " + row[1])
    print("*"*20)


connection.close()


#%% tüm bilgileri çektik
import sqlite3
connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

execute1 = "Select * from customers"

cursor.execute(execute1)

liste = cursor.fetchall()

for i in range(0,len(liste)):
    
    print("Id : ", liste[i][0])
    print("First Name : ", liste[i][1])
    print("Last Name : ", liste[i][2])
    print("Company : ", liste[i][3])
    print("Address : ", liste[i][4])
    print("City : ", liste[i][5])
    print("State : ", liste[i][6])
    print("Country : ", liste[i][7])
    print("Postal Code : ", liste[i][8])
    print("Phone : ", liste[i][9])
    print("Fax : ", liste[i][10])
    print("Email : ", liste[i][11])
    print("Support Rep Id : ", liste[i][12])
    print("*"*50)
connection.close()

#%%praglı müşterileri çekelim

import sqlite3 as sq

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("Select FirstName, LastName from customers where city = 'Prague'")

liste = cursor.fetchall()

for row in liste:
    print("First Name : " + row[0])
    print("Last Name : " + row[1])
    print("*"*50)

print("{} kişi Praglı".format(len(liste)))


