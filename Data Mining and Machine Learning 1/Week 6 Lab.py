# Assignment 1: LR
"""
In the exercise folder you will find a file called regressionExample.csv. Read this file into a NumPy array
Use train_test_split to split the dataset into 20% test and 80% training.
Use LinearRegressor to build a predictive model for the data and assess its accuracy.
"""
# Importing necessary libraries.
from numpy import genfromtxt
from sklearn.model_selection import train_test_split

# First we import the CSV file into a numpy array.
df = genfromtxt('/Users/polinaprinii/Downloads/regressionExample.csv', delimiter= ',')
print(df)

# Secdondly we split the data into 20% test and 80% train. 

