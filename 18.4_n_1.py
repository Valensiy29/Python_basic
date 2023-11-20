import requests
import json

planet = requests.get('https://swapi.dev/api/people/3/')

data = json.loads(planet.text)
data['name'] = 'Valya'

with open('my_json.json','w') as file:
    json.dump(data,file,indent=4)

planet_2 = requests.get("https://swapi.dev/api/planets/8/")
data_2 = json.loads(planet_2.text)
print(data_2)