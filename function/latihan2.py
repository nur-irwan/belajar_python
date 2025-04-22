#latihan mengecek angka ganjil menggunakan function
def cek_Angka(n):
    if n % 2 == 0:
        return "Genap"
    else :
        return "Ganjil"
    
angka = int(input("Masukkan Angka :"))
print("angka tesebut adalah Angka", cek_Angka(angka))