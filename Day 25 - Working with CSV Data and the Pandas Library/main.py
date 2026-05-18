import csv
import pandas

# Read csv data with csv library
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for index in data:
#         if index[1] != 'temp':
#             temperature.append(int(index[1]))
#     print(temperature)

# Read csv with pandas library
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# avg_tmp = sum(temp_list) / len(temp_list)
# print(avg_tmp)
# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in Columns
# print(data["condition"])
# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * (9 / 5) + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Cozz"],
#     "scores": [76, 56, 65]
# }
# data_scratch = pandas.DataFrame(data_dict)
# print(data_scratch)
# data_scratch.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Counts": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrels_count.csv")