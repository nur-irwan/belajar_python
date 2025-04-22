#latihan fungsi menghitung luas segitiga

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi
x = float(input("Masukkan nilai alas:"))
y = float(input("masukkan nilai tinggi:"))
print("Luas segitiga :", luas_segitiga(x,y))