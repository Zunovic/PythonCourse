#import csv
import pandas


# Alter Code wie man csv in Python ausliest ohne Pandas
#
#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()

# print(data_dict)
#
# temp_list = data["temp"].to_list()
# avg_temp = sum(temp_list)/len(temp_list)
#
# print(avg_temp)
#
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# print(data[data.day == "Monday"])
#
## Einen bestimmten Tag suchen, der die max temp hat
# print(data[data.temp == data.temp.max()])


# # Einen Tag ausgeben aber die Temp ist in Fahrenheit statt Celsius
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_fahrenheit = monday_temp * 9/5 + 32
#
# print(monday_temp_fahrenheit)


# # Daten auslesen aus der csv
# cp_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# # cp_data[cp_data] greift auf alle daten zu die in den ["String"] filtern stehen
# gray_sqrl = len(cp_data[cp_data["Primary Fur Color"] == "Gray"])
# red_sqrl = len(cp_data[cp_data["Primary Fur Color"] == "Cinnamon"])
# black_sqrl = len(cp_data[cp_data["Primary Fur Color"] == "Black"])
#
# print(gray_sqrl)
# print(red_sqrl)
# print(black_sqrl)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count":  [gray_sqrl, red_sqrl, black_sqrl],
# }
#
# print(data_dict)
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("sqrl_count.csv")