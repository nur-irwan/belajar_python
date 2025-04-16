#tuple dapat di loop dengan menggunakan perulangan for
thistuple = ("apple", "banana","cherry")
for x in thistuple :
    print(x)
    
#Looping Melalui Nomor Indeks Anda juga dapat melakukan looping melalui item tuple dengan merujuk ke nomor indeksnya. Gunakan fungsi range() dan len() untuk membuat iterable yang sesuai.
thistuple = ("apple","banana","cheryy")
for i in range(len(thistuple)):
    print(thistuple[i])