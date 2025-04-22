#latihan dasar menggunakan fungsi menghitung nilai ujian
def cek_lulus(nilai):
    if nilai >= 70:
        return "Lulus"
    else:
        return "Tidak Lulus"
    
x = int(input("Masukkan NIlai Ujian :"))
print("Hasil Ujian adalah", cek_lulus(x))