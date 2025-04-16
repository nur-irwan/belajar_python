#dalam tuple bisa mengekstrak nilai pada tuple jadi variable, namanya unpack
fruits = ("apple","banana","cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#gunakan * jika nilai variable lebih sedikit dari item
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#==========================
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)