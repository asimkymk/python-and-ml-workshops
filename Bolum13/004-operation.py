# -*- coding: utf-8 -*-
#basic operations
import numpy as np

a = np.array([20,30,40,50])

b = np.arange(4)

print(a)

print(b)

c = a - b #eşit eleman sayısına sahipse çalışır
print(c)
d = b ** 2
print(d)

e = 10 ** np.sin(a)
print(e)
print(e<7)

print(a * b)
print(a@b) # matris çarpımı

print(a.dot(b)) #matris çarpımı 2. yol

f = np.ones((2,4))
g = np.zeros((2,4))
print(f)
print(g)

h = np.random.random((2,4)) # 0 1 arasında rastgele sayılar
print(h)

i = np.sum(b) # b listesini toplar
print(i)

j = np.min(b) # en küçük değer
k = np.max(b) # en büyük değer
print(i)
print(k)

l = np.sqrt(b) # kareköklerini verir
print(l)