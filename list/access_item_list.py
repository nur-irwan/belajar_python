#list dapat di akses dengan menunjuk index nya
thisList = ["apple", "banana","cherry"]
print(thisList[1])
#list bisa menggunakan negatif indexes, dihitung dari belakang
thisList = ["apple","banana","cherry"]
print(thisList[-1])
#list bisa menggunakan range indexes
thisList = ["apple","banana","orange","mango","cherry"]
print(thisList[2:4])

#list juga bisa mencari data di dalamnya menggunakan if
thisList = ["orange","banana","cheryy","mango","kiwi"]
if "mango" in thisList:
    print("Yes, 'mango' is in the fruits list")