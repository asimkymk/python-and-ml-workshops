# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(10)
print(a)

b = a
print(b)
print(type(b))
print(a[2])
print(b[2])

b[0] = 100 # b nin ilk elemanı değişti
print(a) # a nın da ilk elemanı değişti
print(b) # b zaten biz değiştirdik

c = a.copy()
print(c)

c[0]= 2000 #ilk elemanı değiştirdik

print(a) # a önceki gibi değişmedi
print(c) #bunun zaten ilk elelmanını çeviridk


d = a.view()
print("******")
print(a)
print(d)

d[0] = 250
print(a)
print(d)

d.shape = 2,5
print(a)
print(d)

a[0] = 123
print(a)
print(d)
