import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn externals import joblib
from sklearn.metrics import mean_absolute_error

df = pd.read_csv('ml_house_data_set.csv')

# Remove the fields from the data set that we don't want to include in our model
del df['house_number']
del df['unit_number']
del df['street_name']
def df['zip_code']

# Replace categorical data with one-hot encoded data
features_df = pd.get_dummies(df, columns = ['garage_type', 'city'])
del features_df['sale_price']

X = features_df.as_matrix()
y = df['sale_price'].as_matrix()

# Split the data set in a training set (70%) and a test set (30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Create the model
model = ensemble.GradientBoostingRegressor()

# Parameters we want to try
param_grid = {
    'n_estimators': [500, 1000, 3000],
    'max_depth': [4, 6],
    'min_samples_leaf': [3, 5, 9, 17],
    'learning_rate': [0.1, 0.05, 0.02, 0.01],
    'max_features': [1.0, 0.3, 0.1],
    'loss': ['ls', 'lad', 'huber']
}

# define the grid search we want to run
gs_cv = GridSearchCV(model, param_grid, n_jobs=4)

# run the grid search
gs_cv.fit(X_train, y_train)
# print parameters that give us the best results
print gs_cv.best_params_
# After running a .....long..... time, the output will be something like
# {'loss': 'huber', 'learning_rate': 0.1, 'min_samples_leaf': 9, 'n_estimators': 3000, 'max_features': 0.1, 'max_depth': 6}

# That is the combination that worked best.

# find the error rate on the training set using the best parameters
mse = mean_absolute_error(y_train, gs_cv.predict(X_train))
print 'Training set mean absolute error: %.4f' % mse

# find the error rate on the test set using the best parameters
mse = mean_absolute_error(y_test, gs_cv.predict(X_test))
print 'Test set mean absolute error: %.4f' % mse

mse = mean_absolute_error(
