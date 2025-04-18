#hitung huruf vocal pada sebuah kalimat
#1. minta user input kalimat
#2. hitung jumlah huruf vocal pada kalimat
#3. tampilkan hasil nya ke user

kalimat = input("Input Sebuah kalimat :")
vocal = "aiueoAIUEO"
jumlah_vocal = 0
for huruf in kalimat:
    if huruf in vocal:
        jumlah_vocal += 1
print(f"Jumlah Huruf Vocal :", jumlah_vocal)