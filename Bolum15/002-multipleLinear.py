# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

data = pd.read_csv("insurance.csv")
print(data.describe())
#y
expenses = data.expenses.values.reshape(-1,1)
#x
ageBmis = data.iloc[:,[0,2]].values
#test = data[["age","bmi"]].values
regression = LinearRegression()

regression.fit(ageBmis,expenses)

print(regression.predict([[30,20],[30,21],[30,22],[30,23],[30,24]]))
print(r2_score(expenses,regression.predict(ageBmis)))
#%%
plt.scatter(data.age,data.expenses)
x = np.arange(min(data.age),max(data.age)).reshape(-1,1)
age = data.age.values.reshape(-1,1)
regs = LinearRegression()
regs.fit(age,expenses)

plt.plot(x,regs.predict(x),color="red")
plt.title =" expenses depends on ages"
plt.show()

