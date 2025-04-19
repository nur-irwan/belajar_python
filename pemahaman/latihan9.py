#program kategori usia & harga tiket bioskop 
#minta input nama dan usia pengguna
#menentukan kategori usia:
    #0 - 5 tahun: Balita
    #6 - 12 tahun: Anak-anak
    #13 - 17 tahun: Remaja
    #18 - 59 tahun: Dewasa
    #60 tahun ke atas: Lansia
#Menentukan harga tiket bioskop berdasarkan kategori:
    #Balita: Gratis
    #Anak-anak: Rp20.000
    #Remaja: Rp30.000
    #Dewasa: Rp50.000
    #Lansia: Rp25.000

nama = input("Masukkan Nama :")
usia = int(input("Masukkan Usia:"))
#katogori usia
if usia < 0:
    print("usia tidak valid")
else:
    if usia <= 5 :
        kategori_usia = "balita"
        tiket = "gratis"
    elif usia <= 12:
        kategori_usia = "anak-anak"
        tiket = "Rp.20.000"
    elif usia <= 17:
        kategori_usia = "Remaja"
        tiket = "Rp.30.000"
    elif usia <= 58:
        kategori_usia = "Dewasa"
        tiket = "Rp.50.000"
    else :
        kategori_usia = "Lansia"
        tiket = "Rp.25.000"

print(f"Halo {nama.capitalize()}")
print(f"Usia Kamu {usia} tahun, termasuk kategori {kategori_usia}")
print(f"Harga Tiket Bioskop {tiket}")
    