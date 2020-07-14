# -*- coding: utf-8 -*-
"""Salary_predictor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hKQTvtKpmV9-lGeTVH0lU5l9miQMT5Za
"""

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""## Load Data"""

df=pd.read_csv('salary_data.csv')

df.head()

df.tail()

df.shape

"""## Discover and visualize the data to gain insights"""

df.info()

df.describe()

plt.scatter(x = df.Experience_years, y = df. Salary)
plt.xlabel("Employee experience")
plt.ylabel("Employee salary")
plt.title("Scatter plot of Employee Experience years vs Employee salary")
plt.show()

"""## Prepare the data for machine learning Model"""

#datacleaning

df.isnull().sum()

df.mean()

df2=df.fillna(df.mean())

df2.isnull().sum()

df2.head()

df2.tail()

#split dataset

x = df2.iloc[:, :-1].values
y = df2.iloc[:,1].values
print("shape of x = ",x.shape)
print("shape of y= ",y.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y, test_size = 1/3, random_state=0)
print("shape of x_train = ",x_train.shape)
print("shape of y_train = ",y_train.shape)
print("shape of x_test = ",x_test.shape)
print("shape of y_test = ",y_test.shape)

"""#select a model and train it"""

#y = m * x + c
from sklearn.linear_model import LinearRegression
lr=LinearRegression()

lr.fit(x_train,y_train)

lr.coef_

lr.intercept_

y_pred = lr.predict(x_test)
y_pred

"""## Visualise the dataset"""

plt.scatter(x_train, y_train, color = 'red')
# plot the regression line
plt.plot(x_train, lr.predict(x_train), color='blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(x_test, y_test, color = 'red')
# plot the regression line
plt.plot(x_test, lr.predict(x_test), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

pd.DataFrame(np.c_[x_test,y_test,y_pred],columns=["Experience","salary","Predicted_salary"])



"""## Make new prediction"""

new_salary_pred =lr.predict([[15]]).round(2)
print('The predicted salary of a person with 15 years experience is ',new_salary_pred)

"""#Fine tune your model"""

lr.score(x_test,y_test)

"""## Save ML model"""

import joblib
joblib.dump(lr,"Salary_predictor_model.pkl")

model=joblib.load("Salary_predictor_model.pkl")

model.predict([[5]])