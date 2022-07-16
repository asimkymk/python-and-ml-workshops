# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:56:50 2019

@author: Asım
"""

import numpy as np
import pandas as pd

soccer = pd.read_csv("mls-salaries-2017.csv")

print(soccer.head(10))

print(len(soccer.index))

print(soccer["base_salary"].mean())

print(soccer["base_salary"].max())

print(soccer[soccer["guaranteed_compensation"] == soccer["guaranteed_compensation"].max()]["last_name"].iloc[0])
print(soccer[soccer["last_name"] == "Gonzalez Pirez"]["position"].iloc[0])

print(soccer.groupby("position")["base_salary"].mean())

print(soccer["position"].nunique())

print(soccer.groupby("position").size())
print(soccer["position"].value_counts())

print(soccer["club"].value_counts())

print(soccer[soccer["last_name"].str.contains("son")])

print(soccer.index.size)
