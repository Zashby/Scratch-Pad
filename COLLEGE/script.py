# import requests
# import csv
# import os
# import random as rn


# response = requests.get(
#     "https://randomuser.me/api/?results=30&inc=name&nat=us")
# jsonResponse = response.json()['results']

# department = ["Human resources", "information Technology",
#               "Analytics", "Shipping and recieving"]

# awards = ["Performance Award", "Special Commendation Award"]

# dataList = []


# for i, x in enumerate(jsonResponse):
#     tempList = []
#     tempList.append(x["name"]["first"])
#     tempList.append(x["name"]["last"])
#     tempList.append(rn.choice(department))

#     if i % 2 == 0:
#         tempList.append(rn.choice(awards))
#     else:
#         tempList.append("None")

#     dataList.append(tempList)


# with open('namedata.csv', "w+", newline="") as file:
#     csv_writer = csv.writer(file)
#     csv_writer.writerows(dataList)

import random as rn

dataList = [
]
for x in range(11):
    dataList.append(rn.randrange(500, 2000))

print(dataList)
