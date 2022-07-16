# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10 * np.random.random((2,3)))
b = np.floor(10 * np.random.random((2,3)))

print(a)
print(b)

c = np.vstack((a,b)) #dikey olarak birleştirir.
print(c)

d = np.hstack((a,b)) # yatay olarak birleştirir
print(d)

