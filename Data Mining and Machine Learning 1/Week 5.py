# Day 5 Assignment: Outliers Detection
"""
1 In the exercise folder you will find a zip file called outlierData.zip. This
zip file contains a training file called trainOutlier.csv and a test file called test.csv.
This is a regression problem and target value is contained in the last column in each file.
Read this data into your program.
"""

# First we import all necessary Libraries:
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import seaborn as sns
from scipy.stats import zscore
from scipy import stats
import numpy as np

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

# Now we move to identify outliers for both train and test.
sns.boxplot(data=pd.DataFrame(train_features))
plt.show()

sns.boxplot(data=pd.DataFrame(test_features))
plt.show()

# Now we move to remove the identified outliers, we do so using z scores.
#Removing outliers for train dataset
z_scores_train = stats.zscore(train)

abs_z_scores_train = np.abs(z_scores_train)
filtered_entries_train = (abs_z_scores_train < 3).all(axis=1)
new_df_train = train[filtered_entries_train]

# Removing outliers for test dataset
z_scores_test = stats.zscore(test)

abs_z_scores_test = np.abs(z_scores_test)
filtered_entries_test = (abs_z_scores_test < 3).all(axis=1)
new_df_test = test[filtered_entries_train]

# Now we set the features and labels to the new df's after removing the outliers.
# For train df.
new_train_features = new_df_train.iloc[:, :-1].values
new_train_labels = new_df_test.iloc[:, -1].values

# For test df.
new_test_features = new_df_test.iloc[:, :-1].values
new_test_labels = new_df_test.iloc[:, -1].values

# 
