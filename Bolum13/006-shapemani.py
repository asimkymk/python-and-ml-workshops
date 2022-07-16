# -*- coding: utf-8 -*-

#shape manipulation

import numpy as np

a = np.floor(10**np.random.random((3,4)))
print(a)
print(a.shape) # 3 e 4
print(a.ravel()) #düz listeye çevirir
a = a.ravel() # düzleştirdik

print(a)
print(a.shape)
print(a.reshape(2,6)) # 2 satır 6 sütun yaptık
a = a.reshape(2,6)
print(a.T) # yana  çevirdi. yani 6ya 2 oldu


