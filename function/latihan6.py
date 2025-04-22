#latihan function menghitung nilai siswa

#fungsi nilai rata-rata
def hitung_rata2(n1,n2,n3):
    return (n1+n2+n3) / 3

#fungsi cek kelulusan
def cek_lulus(rata2):
    return "Lulus" if rata2 >= 70 else "Tidak lulus"

#fungsi predikat nilai
def predikat(nilai):
    if nilai > 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    else:
        return "D"
    
nama = input("Masukkan Nama Siswa :")
n1 = int(input("Masukkan Nilai 1:"))
n2 = int(input("Masukkan Nilai 2:"))
n3 = int(input("Masukkan Nilai 3:"))

rata2 = hitung_rata2(n1,n2,n3)
status = cek_lulus(rata2)
grade = predikat(rata2)

print("\n===Hasil Ujian===")
print("Nama", nama)
print("Rata-rata Nilai :", rata2)
print("Status :", status)
print("Predikat :", grade)
