import requests
import uuid
import datetime
import json

pixela_endpoint = "https://pixe.la/v1/users"

configuration = json.load(open("configuration.json", "r"))

TOKEN = configuration["TOKEN"]

GRAPH_ID = configuration["GRAPH_ID"]

USERNAME = configuration["USERNAME"]

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


def create_user():
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}


def configure_new_graph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling-Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


def create_pixel_for_the_day():
    pixel_data = {
        "date": datetime.datetime.now().strftime("%Y%m%d"),
        "quantity": "9.74",
    }
    print(requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers).text)


def update_pixel():
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.datetime.now().strftime('%Y%m%d')}"
    new_pixel_data = {
        "quantity": "4.5"
    }
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)

def delete_information():
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{datetime.datetime.now().strftime('%Y%m%d')}"
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)