import random


angka_rahasia = int(random.randint(1,10))
jumlah_tebakan = 0

while True: 
    tebak = int(input("Tebak Angka 1-10:"))
    jumlah_tebakan +=1
    if tebak < angka_rahasia:
        print("Angka Terlalu Kecil")
    elif tebak > angka_rahasia:
        print("Angka Terlalu Besar")
    else:
        print("Kamu Hebat, Jumlah Tebakan =", + jumlah_tebakan)
        break