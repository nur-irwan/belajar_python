#belajar function pada python
#function bikin fungsi lebih rapih, penggunaan berulang, gampang di kembangkan

#struktur dasar function (def)
def sapa():
    print("Halo, Selamat Datang!")
    
sapa() #memanggil fungsi

#function dengan parameter
def sapa_nama(nama):
    print(f"Halo, {nama}")
sapa_nama("Irwan")

#function mengembalikan nilai dengan return
def tambah(a, b):
    return a + b
hasil = tambah(3,5)
print("Hasil :", hasil)