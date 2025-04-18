car = {
    "brand" : "toyota",
    "model" : "kijang inova",
    "year" : 2023
}
x = car.keys()
print(x) #sebelum diubah
car["color"] = "white"
print(x) #setelah diubah
x = car.values()
print(x)