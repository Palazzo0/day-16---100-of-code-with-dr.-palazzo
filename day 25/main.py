# with open("weather_data.csv") as data:
#     data = data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperature = []
#     for row in data:
#         if "temp" not in row[1]:
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas


data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
average = sum(temp_list) / len(temp_list)
print(data["temp"].max())
print(average)

print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
mon_temp_f = monday_temp * 9/5 + 32

print(monday_temp)

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # print(squirrel_data)
# squirrel_color_list = data["Primary Fur Color"].to_list()
# cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
# gray = len(data[data["Primary Fur Color"] == "Gray"])
# black = len(data[data["Primary Fur Color"] == "Black"])
# print(cinnamon)
#
# squirrel_dict ={
#     "color": ["Cinnamon","Gray", "Black"],
#     "count": [cinnamon, gray, black]
# }
#
# new_data = pandas.DataFrame(squirrel_dict)
# new_data.to_csv("squirrel_count.txt")
# print(squirrel_color_list)

