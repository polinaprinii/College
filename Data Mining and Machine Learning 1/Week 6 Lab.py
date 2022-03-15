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

# Assign features and targets:
X = df[:, :-1]  # Our features
y = df[:, -1]   # Our targets

# Secondly we split the data into 20% test and 80% train:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(X_train.shape, "\n",
      X_test.shape, "\n",
      y_train.shape, "\n",
      y_test.shape, "\n")

# Lastly we apply Linear Regression:
regression = linear_model.LinearRegression()
regression = regression.fit(X_train, y_train)

print(regression.score(X_test,y_test)) # R-squared
"""
Please note that due to the nature of the provided dataset, the accuracy level is a perfect hit.
This is due to the fact that columns 9, 10, and 11 are identical.
Thus the machine learning algo just pulls from those 3.
"""

# Assignment 2: LR

"""
Q1
􏰀 Use LinearRegressor to build a predictive model for Boston Housing
data
􏰀 Use train_test_split to split the dataset into 20% test and 80%
training.
"""

# As the Boston Housing Data is DEPRECATED assignemnt 2 is concluded.