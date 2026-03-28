import pandas as pd
from sklearn import linear_model

df=pd.read_csv('data.csv')
x=df[['weight','volume']]
y=df['CO2']

reg=linear_model.LinearRegression()
reg.fit(x,y)

pridictc02=reg.predict([[2300,3000]])

print(pridictc02)

