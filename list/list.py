#belajar list
#list adalah salah satu tipe data dalam python

#cara buat list variable = []
thislist = ["apple","banana","orange"]
print(thislist)

#list dapar berisi item yg sama dala 1 list
thislist = ["apple","banana","apple"]
print(thislist)
#untuk mengetahui panjang dari sebuah list gunakan function len()
thislist = ["apple","banana","cherry"]
print(len(thislist))

#list bisa berisi type data apapun
list1 = ["apple","banana","cherry"]
list2 = [1,2,3,4,5]
list3 = [True, False, True] #type boolean harus diawali huruf besar
print(list1)
print(list2)
print(list3)

#list dalam 1 variable bisa berisi type data yg berbeda
list1 = ["apple",30, True]
print(list1)

#list dapat mengetahui type data yg ada didalamnya
myList = ["apple", "banana", "cherry"]
print(type(myList))