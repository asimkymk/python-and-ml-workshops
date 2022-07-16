# -*- coding: utf-8 -*-
"""
Created on Sat May 11 22:42:07 2019

@author: Asım
"""

import sqlite3 as sq

connection = sq.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("""select albums.Title, artists.name from artists inner join
               albums on artists.ArtistId = albums.ArtistId order by artists.name,
               albums.Title
               """)
liste = cursor.fetchall()

for row in liste:
    print("Albüm   : " + row[0])
    print("Sanatçı : " + row[1])
    print("*"*50)