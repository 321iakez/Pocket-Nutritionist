import requests
import psycopg2

conn = psycopg2.connect(database="testdb", host="localhost", user="postgres", password="postgres")
cur = conn.cursor()

cur.execute("CREATE TABLE pytable (id serial PRIMARY KEY, num integer, data varchar);")
conn.commit()

cur.close()
conn.close()

"""
URL = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY"

food = "ribeye, raw"
common_foods = ["apple, raw"]
PARAMS = {'query': food}
headers = {'Content-Type': 'application/json'}
r = requests.post(url=URL, json=PARAMS)
datalist = r.json()
print(len(datalist['foods'])food1 = datalist['foods'][0]


for x in food1['foodNutrients']:
    print(x['nutrientName'])

"""
