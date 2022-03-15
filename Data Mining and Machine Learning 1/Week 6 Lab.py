# Assignment 1: LR
"""
In the exercise folder you will find a file called regressionExample.csv. Read this file into a NumPy array
Use train_test_split to split the dataset into 20% test and 80% training.
Use LinearRegressor to build a predictive model for the data and assess its accuracy.
"""
# Importing necessary libraries.
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import pandas as pd

# First we import the CSV file into a numpy array.
df = genfromtxt('/Users/polinaprinii/Downloads/regressionExample.csv', delimiter= ',')

# Next we convert the numpy array to a pandas dataframe.
pd_df = pd.DataFrame(df)
#print(pd_df.info, "\n")
#print(pd_df.describe(), "\n")
#print( pd_df.head(), "\n")

# # Assign features and labels:
# X = df[:, :-1]
# y = df[:, -1]
#
# # Secondly we split the data into 20% test and 80% train:
# X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=5)
# print(X_train.shape, "\n",
#       X_test.shape, "\n",
#       Y_train.shape, "\n",
#       Y_test.shape, "\n")
#
# # Lastly we apply Linear Regression:
# regression = linear_model.LinearRegression()
# regression.fit(X_train, Y_train)
#
# #Y_pred = regression.predict(X_test)
#
# print(regression.score(X_test,Y_test)) # R-squared
# #print("Mean squared error: %.3f"
#       #% mean_squared_error(Y_test, Y_pred))

