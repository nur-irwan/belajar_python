#calculator dengan fungsi pada python
def tambah(a,b):
    return a + b
def kurang(a,b):
    return a - b
def kali(a,b):
    return a*b
def bagi(a,b):
    return a/b 

#tes
x = int(input("Masukkkan Angka Pertama:"))
y = int(input("Masukkan Angka Kedua :"))

print("Tambah :", tambah(x,y))
print("kurang :", kurang(x,y))
print("kali :", kali(x,y))
print("bagi :", bagi(x,y))