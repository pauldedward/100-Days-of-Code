import pandas

# with open() as data:
# content = pandas.read_csv("./Day-25/data.csv")

# data = content.to_dict()
# print(data)

# csv_data = pandas.DataFrame(data)
# csv_data.to_csv("./Day-25/new_data.csv")

data = pandas.read_csv("./Day-25/squirrel.csv")

black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])

data_object = {
    "Color": ["Black", "Red", "Gray"],
    "Count": [black_squirrels, red_squirrels, grey_squirrels]
}

pandas.DataFrame(data_object).to_csv("./Day-25/squ_data.csv")