#fungsi dalam fungsi

def luar():
    def dalam():
        print("ini dari fungsi dalam.")
    print("ini fungsi dari luar.")
    dalam() #memanggil fungsi dari dalam fungsi luar
luar()

#untuk menjaga struktur ralih
#akses variabel dari fungsi luar
#dasar konsep closure

#contoh hitung luas lingkaran
def hitung_luas_lingkaran(jari_jari):
    def kuadrat(x):
        return x * x
    pi = 3.14
    return pi * kuadrat(jari_jari)

print(hitung_luas_lingkaran(7))