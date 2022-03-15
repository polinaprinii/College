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

# Assign features and labels:
train_data, labels = df[:, :-1], df[:, -1]

# Secondly we split the data into 20% test and 80% train:
X_train, X_test, Y_train, Y_test = train_test_split(train_data, labels, test_size=0.2, random_state=5)
print(X_train.shape, "\n",
      X_test.shape, "\n",
      Y_train.shape, "\n",
      Y_test.shape, "\n")

# Lastly we apply Linear Regression:


