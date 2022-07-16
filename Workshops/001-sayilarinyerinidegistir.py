# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 02:37:14 2019

@author: Asım
"""


x = 10
y = 20

#x ve y nin yerini değiştir
#yol-1

print("x: {} ve y: {}".format(x,y))

x1 = x
y1 = y
x = y1
y = x1

print("x: {} ve y: {}".format(x,y))

#yol-2
x = 10
y = 20

print("x: {} ve y: {}".format(x,y))

x,y=y,x
print("x: {} ve y: {}".format(x,y))