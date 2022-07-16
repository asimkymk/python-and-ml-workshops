# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:26:17 2019

@author: Asım
"""

import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("""Update customers set city = 'İstanbul', firstName = 'Adem' 
               where city = 'Bayburt'
               """)
connection.commit()

connection.close()