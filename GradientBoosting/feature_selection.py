import numpy as np
from sklearn.externals import joblib

feature_labels = np.array(['year_built', 'stories', 'num_bedrooms', 'full_bathrooms',
                           'half_bathrooms', 'livable_sqft', 'total_sqft', 'garage_sqft',
                           'carport_sqft', 'has_fireplace', 'has_pool', 'has_central_heating',
                           'has_central_cooling', 'garage_type_attached', 'garage_type_detached',
                           'garage_type_none', 'city-Amystad', 'city-Brownport', 'city-Chadstad',
                           'city-Clarkberg', 'city-Coletown', 'city-Davidfort', 'city-Davidtown',
                           'city-East Amychester', 'city-East Janiceville', 'city_East Justin', 'city_East Lucas',
                           'city_Fosterberg', 'city_Hallfort', 'city_Jeffreyhaven',
                           'city_Jenniferberg', 'city_Joshuafurt', 'city_Julieberg',
                           'city_Justinport', 'city_Lake Carolyn', 'city_Christinaport',
                           'city_Lake Dariusborough', 'city_Lake Jack', 'city_Lake Jennifer', 'city_Leahview',
                           'city_Lewishaven', 'city_Martinezfort', 'city_Morrisport', 'city_New Michele',
                           'city_New Robinton', 'city_North Erinville', 'city_Port Adamtown',
                           'city_Port Andrealand', 'city_Port Daniel', 'city_Port Jonathanborough',
                           'city_Richardport', 'city_Rickytown', 'city_Scottberg', 'city_South Anthony',
                           'city_South Stevenfurt', 'city_Toddshire', 'city_Wendybury', 'city_West Ann',
                           'city_West Brittanyview', 'city_West Gerald', 'city_West Gregoryview',
                           'city_West Lydia', 'city_West Terrence'])

model = joblib.load('trained_house_classifier_model.pkl')
importance = model.feature_importances_

feature_indexes_by_importance = importance.argsort()

for index in feature_indexes_by_importance:
    print '{} - {: .2f}%'.format(feature_labels[index], (importance[index] * 100.0))
    
