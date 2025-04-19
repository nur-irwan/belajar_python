#Buat program kasir sederhana untuk sebuah toko. Program harus:   
#Meminta input:
#Nama pelanggan
#Nama barang
#Harga barang
#Jumlah beli
#Hitung total belanja:
#total = harga × jumlah
#Jika total belanja:
#Di atas Rp500.000 → Diskon 15%
#Di atas Rp300.000 → Diskon 10%
#Di atas Rp100.000 → Diskon 5%
#Selain itu, tidak ada diskon
print("=======Program Kasir Sederhana========")
while True:
    nama_pelanggan = input("Masukkan Nama :")
    nama_barang = input("Masukkan Nama Barang :")
    harga_barang = int(input("Masukkan Harga Barang :"))
    jumlah_beli = int(input("Jumlah Beli :"))

    total = harga_barang * jumlah_beli
    if total >= 500000:
        diskon = total * (15/100)
        persen = "15%"
    elif total >= 300000:
        diskon = total * (10/100)
        persen = "10%"
    elif total >= 100000:
        diskon = total * (5/100)
        persen = "5%"
    else :
        diskon = 0
        persen = "0%"

    total_bayar = total - diskon
    print("===STRUK PEMBAYARAN===")
    print(f"Nama Pelanggan : {nama_pelanggan}")
    print(f"Barang Dibeli : {nama_barang}")
    print(f"Harga Satuan : {harga_barang}")
    print(f"Jumlah Beli : {jumlah_beli}")
    print(f"Total Sebelum Diskon : Rp.{total:,}")
    print(f"Diskon {persen} : Rp.{diskon:,}")
    print(f"Total Bayar : Rp.{total_bayar:,}")

    #tanya apakah ingin beli lagi
    lagi = input("Apakah ingin belanja lagi? (y/n):")
    if lagi.lower() != "y":
        print("Terima Kasih sudah berbelanja")
        break