class FlightData:
    def __init__(self, city_from, city_to, fly_from, fly_to, date_from, date_to, price):
        self.city_from = city_from
        self.city_to = city_to
        self.fly_from = fly_from
        self.fly_to = fly_to
        self.date_from = date_from
        self.date_to = date_to
        self.price = price

    def __str__(self):
        return f"{self.__dict__}"
