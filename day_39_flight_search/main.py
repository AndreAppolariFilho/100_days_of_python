#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import data_manager
from flight_search import FlightSearch
from pprint import pprint
from datetime import datetime, timedelta
import json

if __name__ == "__main__":
    configuration = json.load(open("configurations.json"))
    sheet_data_manager = data_manager.DataManager("flight_deals_prices.csv")
    sheet_data = sheet_data_manager.load_data()
    flight_data_search = FlightSearch(
        app_id=configuration["flight_app_id"],
        app_key=configuration["flight_app_key"]
    )
    departing_city = flight_data_search.search_iata_code("Lisbon")
    tomorrow = datetime.now() + timedelta(days=1)
    six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
    for row in sheet_data:
        row["IATA Code"] = flight_data_search.search_iata_code(row["City"])

    sheet_data_manager.upload_data(sheet_data)
    for row in sheet_data:
        flight = flight_data_search.search_prices(
            city_from=departing_city,
            city_to=row["IATA Code"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        print(flight)
