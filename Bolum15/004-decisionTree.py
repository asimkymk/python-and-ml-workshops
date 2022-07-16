# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv("positions.csv")

level = data.iloc[:,1:2].values.reshape(-1,1)
salary = data.iloc[:,2].values.reshape(-1,1)

regression = DecisionTreeRegressor()

regression.fit(level,salary)

print(regression.predict([[8.9]]))

plt.scatter(level,salary,color = "red")
x = np.arange(min(level),max(level),0.01).reshape(-1,1)
plt.plot(x,regression.predict(x),color="blue")
plt.title = "Decision Tree Model"
plt.xlabel = "Level"
plt.ylabel = "Salary"
plt.show()