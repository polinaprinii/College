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
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.neighbors import KNeighborsRegressor
from mlxtend.data import iris_data
from mlxtend.evaluate import bias_variance_decomp


# Importing data:
data = iris_data()

# Seperate feautures and labels:
X, y = data

# Split data into train and test data:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# a) Decision Tree Classifier:
# Define the model:
modelA = DecisionTreeClassifier()

# Calculate the average expected loss, bias and variance.
avg_expected_loss, avg_bias, avg_var = bias_variance_decomp(
        modelA, X_train, y_train, X_test, y_test,
        loss='0-1_loss',
        random_seed=123)

# Print results:
print('Average expected loss: %.3f' % avg_expected_loss)
print('Average bias: %.3f' % avg_bias)
print('Average variance: %.3f' % avg_var)

# b) Ensemble (Bagging classifier)