# -*- coding: utf-8 -*-

import numpy as np

arr = np.arange(1,10)
print(arr)
print(arr[0])
print(arr[1:5])
print(arr[:4])
print(arr[::2])
print(arr[:3])
arr[:3] = 25
print(arr)

arr = np.arange(1,10)
arr2  = arr

arr2[:3] = 100
print(arr2)
print(arr) # arr2 yi değiştirdik arr de değişti


arr = np.arange(1,10)
arr2 = arr.copy()
arr2[:3] = 100
print(arr2)
print(arr)


newArray = np.arange(1,21)
newArray = newArray.reshape(5,4)
print(newArray)
print(newArray[:,:2])
print(newArray[:3,:3])
print(newArray[:2])

arr = np.arange(1,11)
print(arr >3)

booleanArray = arr > 3

print(arr[booleanArray])


print(arr[arr>5])