# Python V 3.9.0

items = []
cherry = ["small", "red", "cherry"]
pea = ["small", "green", "pea"]
watermelon = ["large", "green", "watermelon"]
pumpkin = ["large", "orange", "pumpkin"]

items.append(cherry)
items.append(pea)
items.append(watermelon)
items.append(pumpkin)

for item in items:
    if item[0] == "small":
        print(item[2] + " is small")
    if item[1] == "green":
        print(item[2] + " is green")