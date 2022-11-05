# comma seperated value

import pandas

data = pandas.read_csv("23-day/228 2018-Central-Park-Squirrel"
                       "-Census-Squirrel-Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
Cin = len(data[data["Primary Fur Color"] == "Cinnamon"])

dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray, black, Cin]}
df = pandas.DataFrame(dict)

df.to_csv("23-day/squ.csv")
