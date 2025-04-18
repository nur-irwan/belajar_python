# latihan menghitung nilai rata-rata
#1. buat list berisi beberapa nilai ( misalnya nilai ujian)
#2. hitung jumlah seluruh nilai
#3. hitung nilai rata-rata
#4. tampilkan hasilnya

nilaiUjian = [80,70,90,100,60,50]
#hitung total
total = 0
for n in nilaiUjian:
    total += n
    
#hitung rata-rata
ratarata = total / len(nilaiUjian)

#tampilkan hasil
print("total nilai: ", total)
print("Nilai rata-rata:", ratarata)