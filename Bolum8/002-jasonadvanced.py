# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:49:10 2019

@author: Asım
"""

import json

with open("users.json") as users:
    data = json.load(users)
    
    for x in range(0,6):
        
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print(data[x]["address"]["geo"]["lat"])
        print("\n")