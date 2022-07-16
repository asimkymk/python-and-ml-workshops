# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 19:22:49 2019

@author: Asım
"""

lights = ["red","yellow","green"]
currentLight = lights[1]

print(currentLight)

if currentLight == "red":
    print("Stop!")
elif currentLight == "yellow":
    print("Ready!")
else:
    print("Go!")