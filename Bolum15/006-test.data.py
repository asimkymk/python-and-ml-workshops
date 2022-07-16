import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
data = pd.read_csv("weight-height.csv")
print(data.columns)
regressionAll = LinearRegression()
heightAll = data.Height.values.reshape(-1,1) * 0.0254
weightAll = data.Weight.values.reshape(-1,1) * 0.4535923

regressionAll.fit(heightAll,weightAll)

#plt.scatter(heightAll,weightAll,color = "red")
#plt.plot(heightAll,regressionAll.predict(heightAll),color="green")
#plt.title = "All Heights - Weights"
#plt.show()
#only males
heightMale = data[data["Gender"] == "Male"]["Height"].iloc[:].values.reshape(-1,1) * 0.0254
weightMale = data[data["Gender"] == "Male"]["Weight"].iloc[:].values.reshape(-1,1) * 0.4535923

regressionMale = LinearRegression()
regressionMale.fit(heightMale,weightMale)

#◘only females
heightFemale = data[data["Gender"] == "Female"]["Height"].iloc[:].values.reshape(-1,1) * 0.0254
weightFemale = data[data["Gender"] == "Female"]["Weight"].iloc[:].values.reshape(-1,1) * 0.4535923

regressionFemale = LinearRegression()
regressionFemale.fit(heightFemale,weightFemale)
print(regressionAll.predict([[2]]))
print(r2_score(weightAll,regressionAll.predict(heightAll)))
print(regressionMale.predict([[2]]))
print(r2_score(weightMale,regressionMale.predict(heightMale)))
print(regressionFemale.predict([[2]]))
print(r2_score(weightFemale,regressionFemale.predict(heightFemale)))
