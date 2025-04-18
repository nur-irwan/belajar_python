#latihann pemahaman percabangan if elif else
#hitung angka diskon
total_belanja = int(input("Masukkan Nominal Belanja :"))

if total_belanja >= 500000:
    diskon = int(total_belanja * (20 / 100))
    print("Diskon 20% :", diskon)
    bayar = total_belanja - diskon
    print("Total yg harus dibayar :", bayar)
elif total_belanja >= 300000:
    diskon = int(total_belanja * (10 / 100))
    print("Diskon 10% :", diskon)
    bayar = total_belanja - diskon
    print("Total yg harus dibayar :", bayar)
else:
    print("maaf belum dapet diskon")