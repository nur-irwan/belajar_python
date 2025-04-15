#untuk menambah item di akhir pada list gunakan function append()
thisList = ["apple","banana","cherry"]
thisList.append("mango")
print(thisList)
#untuk input item pada list di index tertentu gunakan method insert()
thisList = ["apple","banana","cherry"]
thisList.insert(1, "mango")
print(thisList)
#untuk menampilkan list lain pada list yg ingin di cetak bisa gunakan method extend()
list = ["banana","orange","mango"]
list2 = ["papaya","nanas","anggur"]
list.extend(list2)
print(list)

