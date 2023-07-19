import requests
import json

configuration_json = json.load(open("configuration.json"))
natural_exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

API_ID = configuration_json["NUTRITIONIX_APP_ID"]
API_KEY = configuration_json["NUTRITIONIX_APP_KEY"]
GENDER = "m"
WEIGHT_KG = 55
HEIGHT_CM = 180
AGE = 26
headers = {
    "X-APP-ID": API_ID,
    "X-APP-KEY": API_KEY
}
query = input("Tell me which exercises you did: ")
params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(natural_exercise_url, json=params, headers=headers)
result = response.json()
print(result)