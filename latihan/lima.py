#minta user masukkan sebuah bilangan batas atas ex : 100

batas = int(input("Masukkan Batas Angka :"))
print("\nBilangan Genap :")
for i in range(1,batas + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\nBilangan Ganjil :")
for i in range(1, batas + 1):
    if i % 2 != 0:
        print(i, end=" ")