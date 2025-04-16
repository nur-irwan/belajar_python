#cara add,remove item pada tuple
#add
thistuple = ("apple","banana","orange","mango")
y = list(thistuple)
y.append("cherry")
thistuple = tuple(y)
print(thistuple)

#remove
thistuple = ("apple","banana","orange","mango")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
