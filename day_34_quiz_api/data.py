import requests
import html


question_data = requests.get(
    url="https://opentdb.com/api.php",
    params={
        "amount": 10,
        "category": 18,
        "type": "boolean"
    }).json()["results"]

for row in question_data:
    row["question"] = html.unescape(row["question"])