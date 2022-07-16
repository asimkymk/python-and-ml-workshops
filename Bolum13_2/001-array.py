# -*- coding: utf-8 -*-

import numpy as np

data = [1,2,3]
print(data)

arr = np.array(data)
print(arr)

arr2 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr2)

print(arr2[0,1])
print(arr2[:,:1])

print(np.arange(10,20))

print(np.arange(0,100,3))

print(np.zeros(10))

print(np.ones((2,5)))

print(np.linspace(0,100,5))

print(np.linspace(0,1,6))

print(np.eye(6))

print(np.random.randint(0,10))

print(np.random.randint(1,10,5))

print(np.random.randn(5)) #◙eksi sayılar da dahil

arr5 = np.arange(25)
print(arr5)

arr5 = arr5.reshape(5,5)

print(arr5)


newArray = np.random.randint(1,100,10)
print(newArray)
print(newArray.min())
print(newArray.max())
print(newArray.sum())
print(newArray.mean())


detArray = np.random.randint(1,100,25)
detArray = detArray.reshape(5,5)
print(detArray)
print(np.linalg.det(detArray)) # determinant buluyor

detArray2 = np.array([[1,2],[3,4]])
print(detArray2)
print(np.linalg.det(detArray2))
print(round(np.linalg.det(detArray2)))



