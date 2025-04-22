#latihan function dengan menemukan nilai terbesar
def bilangan_terbesar(a, b, c):
    return max(a, b, c)

# input
x = int(input("Masukkan angka pertama: "))
y = int(input("Masukkan angka kedua: "))
z = int(input("Masukkan angka ketiga: "))

# output
print("Bilangan terbesar adalah:", bilangan_terbesar(x, y, z))