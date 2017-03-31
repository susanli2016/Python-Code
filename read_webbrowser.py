import pandas as pd
import webbrowser
import os

data_table = pd.read_csv('ml_house_data_set.csv')
# Create a webpage view of the data for easying viewing
html = data_table[0:100].to_html()
# save html to a temporary file
with open('data.html', 'w') as f:
    f.write(html)
# Open the web page in our web browser
full_filename = os.path.abspath('data.html')
webbrowser.open('file://{}'.format(full_filename))
 
