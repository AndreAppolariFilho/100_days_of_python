import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def search_iata_code(self, city):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": self.app_key}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_prices(self, city_from, city_to, from_time, to_time):
        headers = {"apikey": self.app_key}
        query = {
            "fly_from": city_from,
            "fly_to": city_to,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "EUR"
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query
        )
        try:
            data = response.json()["data"][0]
        except IndexError or KeyError:
            print(f"No flights found for {city_to}")
            return None
        flight_data = FlightData(
            city_from=city_from,
            city_to=city_to,
            fly_from=data["route"][0]["flyFrom"],
            fly_to=data["route"][0]["flyTo"],
            date_from=data["route"][0]["local_departure"].split("T")[0],
            date_to=data["route"][1]["local_departure"].split("T")[0],
            price=data["price"]
        )
        return flight_data