"""
This week we will see how bias, variance and total error vary across different learning algorithms.
We will be testing the following algorithms:
a.	Decision Tree Classifier
b.	Ensemble (Bagging classifier)
c.	Decision Tree Regressor
d.	Ensemble (Bagging Regressor)
e.	K-NN with different values of K
"""

# The dataset will be derived from the mlxtend library.

# Importing all necessary libraries:
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.neighbors import KNeighborsRegressor

