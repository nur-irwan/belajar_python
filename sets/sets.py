#Set adalah salah satu dari 4 tipe data bawaan dalam Python yang digunakan untuk menyimpan koleksi data, 3 lainnya adalah List, Tuple, dan Dictionary, semuanya dengan kualitas dan penggunaan yang berbeda.
#Set adalah koleksi yang tidak berurutan, tidak dapat diubah*, dan tidak terindeks.
#Note: Set items are unchangeable, but you can remove items and add new items.
#=== Cara buat Set =====
thisset = {"apple","banana","orange"}
print(thisset)
# items pada set tidak bole sama
thisset = {"apple","banana","orange","apple"}
print(thisset)
#nilai true dan 1 dikenali sebagai duplikat pada sets
thisset = {"apple","banana", True, 1}
print(thisset)
#gunakan method len() untuk mendapatka nilai pada sets
thisset = {"apple","banana", True, 1}
print(len(thisset))
#tipe data pada sets
set1 = {"orange","banana", "cherry"}
set2 = {1,2,3,4,5,6}
set3 = {True, False, False}
print(set1)
print(set2)
print(set3)