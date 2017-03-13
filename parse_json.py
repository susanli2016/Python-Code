import json
import urllib


locu_api = '9fb8cd70cb34cab8e83690473133f51943b5c93f'

def locu_search(query):
    api_key = locu_api
    url = 'https://api.locu.com/v1_0/venue/search/?api_key=' + api_key
    locality = query.replace(' ', '%20')
    final_url = url + "&locality=" + locality + "&category=restaurant"
    response = urllib.urlopen(final_url).read()
    json_obj = str(response)
    data = json.loads(json_obj)
    for item in data['objects']:
        print(item['name'], item['phone'])
locu_search('Boston')
