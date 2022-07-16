# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:42:07 2019

@author: Asım
"""

import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("Delete from customers where firstName = 'Adem'")
connection.commit()
connection.close()