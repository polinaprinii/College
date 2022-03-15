# Day 5 Assignment: Outliers Detection
"""
1 In the exercise folder you will find a zip file called outlierData.zip. This
zip file contains a training file called trainOutlier.csv and a test file called test.csv.
This is a regression problem and target value is contained in the last column in each file.
Read this data into your program.
"""

# First we import all necessary Libraries:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Next we define our datasets
train = pd.read_csv('/Users/polinaprinii/Downloads/Lab -- Outliers Detection/trainOutlier.csv')
test = pd.read_csv('/Users/polinaprinii/Downloads/Lab -- Outliers Detection/test.csv')

# See the structure of each dataset
train.shape
test.shape

# See the first 5 rows
train.head()
test.head()

# We now split both the train and test data into features and labels.
train_features = train.iloc[:, :-1].values
train_labels = train.iloc[:, -1].values
# We must add .values to all features and labels to avoid FutureWarnings as we are working with data with no headings.
test_features = test.iloc[:, :-1].values
test_labels = test.iloc[:, -1].values

# Now we apply a Decision Tree Regression to assess accuracy.
reg = DecisionTreeRegressor()
reg = reg.fit(train_features, train_labels)
print("The Decision Tree Regression Accuracy is: ", round(reg.score(test_features, test_labels), 2),
      "which as a percentage is: ", round(reg.score(test_features, test_labels), 2) * 100, "%", "\n"
      "Please note we have not yet addressed any outliers.", "\n")

