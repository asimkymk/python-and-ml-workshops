# -*- coding: utf-8 -*-
"""
Created on Sat May 11 19:26:17 2019

@author: Asım
"""

import sqlite3 as sq

connection = sq.connect("chinook.db")
                        
cursor = connection.cursor()
                        
cursor.execute("""Insert into customers
               (firstName, lastName, city,email)
               values ('Asım', 'Kaymak', 'Bayburt','kaymakasm@gmail.com')
               """)
connection.commit()
connection.close()