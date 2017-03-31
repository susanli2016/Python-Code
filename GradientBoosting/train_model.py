import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.externals import joblib
from sklearn.metrics import mean_absolute_error
df = pd.read_csv('ml_house_data_set.csv')
del df['house_number']
del df['unit_number']
del df['street_name']
del df['zip_code']

features_df = pd.get_dummies(df, columns=['garage_type', 'city'])

del features_df['sale_price']

X = features_df.as_matrix()
y = df['sale_price'].as_matrix()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = GradientBoostingRegressor(
    n_estimators = 1000,
    learning_rate = 0.1,
    max_depth = 6,
    min_samples_leaf = 9,
    max_features = 0.1,
    loss = 'huber'
    )

model.fit(X_train, y_train)

# joblib.dump(model, 'trained_house_classifier_model.pkl')

mse = mean_absolute_error(y_train, model.predict(X_train))
print 'Training set mean absolute error: %.4f' % mse
mse = mean_absolute_error(y_test, model.predict(X_test))
print 'Test set mean absolute error: %.4f' % mse


