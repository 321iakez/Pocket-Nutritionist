import requests

URL = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY"

food = "apple, raw"

PARAMS = {'query': food}
headers = {'Content-Type': 'application/json'}
r = requests.post(url=URL, json=PARAMS)
datalist = r.json()
print(len(datalist['foods']))
food1 = datalist['foods'][0]

for x in food1['foodNutrients']:
    print(x['nutrientName'])
