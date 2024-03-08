import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model


df = pd.read_csv("ML\homelook.csv")

plt.xlabel('area(sqr ft)')
plt.ylabel('price(US$)')
plt.scatter(df.area, df.price, color='red',marker='+')

reg = linear_model.LinearRegression()
reg.fit(df[['area']], df.price)

reg.predict(3300)

plt.show()