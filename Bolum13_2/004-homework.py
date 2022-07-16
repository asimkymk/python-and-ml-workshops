# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 00:16:12 2019

@author: Asım
"""

import numpy as np

arr1 = np.ones(5)
print(arr1)

arr2 = np.zeros(5)
print(arr2)

arr3 = np.arange(2,100,2)
print(arr3)

arr4 = np.linspace(10,10,5)
print(arr4)

arr5 = np.arange(1,17).reshape(4,4)
print(arr5)

arr6 = np.eye(4)
print(arr6)

num = np.random.rand() *5
print(num)

arr7 = np.random.randn(25).reshape(5,5)
print(arr7)

arr8 = np.linspace(1,5,20)
print(arr8)

arr9 = np.arange(1,101).reshape(10,10)
print(arr9[4:])

print(arr9[6:,4:])

print(arr9[:3,2:4])

print(arr9[:3,1])

print(arr9[:3,1:2])
print(arr9[:,-1])


arr10 = ((np.random.rand(9) * 5).astype(int)).reshape(3,3)
arr11 = ((np.random.rand(9) * 5).astype(int)).reshape(3,3)
print(arr10)
print(arr11)

print(arr10 + arr11)

print(arr10 * arr11)

print(np.mean(arr10 + arr11))

np

