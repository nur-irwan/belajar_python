#Buat program sederhana:
#Minta input nilai ujian (0–100)
#Tampilkan hasil:
#Nilai ≥ 90: A
#Nilai ≥ 80: B
#Nilai ≥ 70: C
#Nilai < 70: D

nilai = int(input("Masukkan Nilai Ujian :"))
if nilai >= 90:
    print("Nilai Anda A")
elif nilai >= 80:
    print("Nilai Anda B")
elif nilai >= 70:
    print("Nilai Anda C")
else :
    print("Nilai Anda D")