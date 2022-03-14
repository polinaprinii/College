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

# Next we define our datasets
train = pd.read_csv('/Users/polinaprinii/Downloads/Lab -- Outliers Detection/trainOutlier.csv')
test = pd.read_csv('/Users/polinaprinii/Downloads/Lab -- Outliers Detection/test.csv')

# Sanity check to see the data is correctly importing.
print(train.head, "\n")
print(test.head, "\n")