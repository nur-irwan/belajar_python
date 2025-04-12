#looping dalam list
buah = ["apel","jeruk","mangga"]
for item in buah:
    print("buah " + item)
#loopong dengan enumerate(), untuk dapat nilai index
for index, item in enumerate(buah):
    print(f"{index}. {item}")
    