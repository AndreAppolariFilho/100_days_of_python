import csv

#with open("weather_data.csv") as f:
#    data = csv.reader(f)
#    temperatures = []
#    for i, row in enumerate(data):
#        if i != 0:
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas
import pandas as pd

#dataframe = pandas.read_csv("weather_data.csv")

#print(dataframe["temp"])

#data_dict = dataframe.to_dict()
#print(data_dict)

#print(dataframe["temp"].mean())

#print(dataframe["temp"].max())

#print(dataframe[dataframe.day == "Monday"])
#print(dataframe[dataframe.temp == dataframe["temp"].max()])

#monday_temperature = dataframe[dataframe.day == "Monday"]["temp"][0]
#print((monday_temperature * 1.8)+32)

dataframe = pandas.read_csv("2018_Squirrel_Data.csv")
grouped_dict = dataframe.groupby(by=["Primary Fur Color"])["Primary Fur Color"].count().to_dict()

new_dataframe = pd.DataFrame(
    {
        "fur color": [g for g in grouped_dict],
        "total": [grouped_dict[g] for g in grouped_dict],

    }
)
new_dataframe.to_csv("result_squirrels.csv")