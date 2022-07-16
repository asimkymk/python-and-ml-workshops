# -*- coding: utf-8 -*-
"""
Created on Sat May 11 17:50:35 2019

@author: Asım
"""
#%% guplama
import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("""Select city,count(*) from customers group by city 
               order by count(*), city asc""")

liste  = cursor.fetchall()

for row in liste:
    print("City  : " + row[0])
    print("Count : " + str(row [1]))
    print("*"*50)
    
#%%having by yönetemi
import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("""Select city,count(*) from customers group by city
               having count(*) > 1
               order by count(*), city asc""")

liste  = cursor.fetchall()

for row in liste:
    print("City  : " + row[0])
    print("Count : " + str(row [1]))
    print("*"*50)
    