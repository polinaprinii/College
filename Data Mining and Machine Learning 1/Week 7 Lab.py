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
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.neighbors import KNeighborsClassifier
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
avg_expected_loss_A, avg_bias_A, avg_var_A = bias_variance_decomp(
    modelA, X_train, y_train, X_test, y_test,
    loss='0-1_loss',
    random_seed=123)

# Print results:
print("Model results for the Decision Tree Classifier is as follows:")
print('Average expected loss: %.3f' % avg_expected_loss_A)
print('Average bias: %.3f' % avg_bias_A)
print('Average variance: %.3f' % avg_var_A, "\n")

# b) Ensemble (Bagging classifier)
modelB = BaggingClassifier(base_estimator=modelA,
                           n_estimators=100,
                           random_state=123)

# Calculate the average expected loss, bias and variance.
avg_expected_loss_B, avg_bias_B, avg_var_B = bias_variance_decomp(
    modelB, X_train, y_train, X_test, y_test,
    loss='0-1_loss',
    random_seed=123)

# Print results:
print("Model results for the Ensemble Bagging Classifier is as follows:")
print('Average expected loss: %.3f' % avg_expected_loss_B)
print('Average bias: %.3f' % avg_bias_B)
print('Average variance: %.3f' % avg_var_B, "\n")

# c) Decision Tree Regressor:
modelC = DecisionTreeRegressor(random_state=123)

# Calculate the average expected loss, bias and variance.
avg_expected_loss_C, avg_bias_C, avg_var_C = bias_variance_decomp(
    modelC, X_train, y_train, X_test, y_test,
    loss='mse',
    random_seed=123)

# Print results:
print("Model results for the Decision Tree Regressors is as follows:")
print('Average expected loss: %.3f' % avg_expected_loss_C)
print('Average bias: %.3f' % avg_bias_C)
print('Average variance: %.3f' % avg_var_C, "\n")

# d) Ensemble (Bagging Regressor):
modelD = BaggingRegressor(base_estimator=modelC,
                          n_estimators=100,
                          random_state=123)

# Calculate the average expected loss, bias and variance.
avg_expected_loss_D, avg_bias_D, avg_var_D = bias_variance_decomp(
    modelC, X_train, y_train, X_test, y_test,
    loss='mse',
    random_seed=123)

# Print results:
print("Model results for the Ensemble (Bagging Regressor) is as follows:")
print('Average expected loss: %.3f' % avg_expected_loss_D)
print('Average bias: %.3f' % avg_bias_D)
print('Average variance: %.3f' % avg_var_D)

# e) K-NN with different values of K

bias_knn, var_knn, error_knn = [], [], []

# Calculate the average expected loss, bias and variance.
for k in range(1, 15):
    modelE = KNeighborsClassifier(n_neighbors=k)
    avg_expected_loss_E, avg_bias_E, avg_var_E = avg_expected_loss_E, avg_bias_E, avg_var_E = bias_variance_decomp(
        modelE, X_train, y_train, X_test, y_test, loss='mse', random_seed=123)
    bias_knn.append(avg_bias_E)
    var_knn.append(avg_var_E)
    error_knn.append(avg_expected_loss_E)
plt.plot(range(1, 15), error_knn, 'b', label='total_error')
plt.plot(range(1, 15), bias_knn, 'k', label='bias')
plt.plot(range(1, 15), var_knn, 'y', label='variance')
plt.legend()
plt.show()
