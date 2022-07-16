# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:04:44 2019

@author: Asım
"""

import numpy as np


a = np.arange(15).reshape(3,5) #15 elemanlı ndarray oluşur liste gibi 3 satır 5lik
print(a)
print(type(a))
print("Dimension Count = " , str(a.ndim)) #kaç boyutlu

b = np.arange(10)
print(b.shape)
print(b)
print(b.ndim)