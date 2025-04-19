print("====Program Indeks Massa Tubuh ====")
while True:
    nama = input("Masukkan Nama :")
    berat = float(input("Masukkan Berat Badan (kg):"))
    tinggi = float(input("Masukkan Tinggi Badan (M):"))
    
    if berat <= 0 or tinggi <=0:
        print("berat dan tinggi tidak bole 0")
        break
    #menentukan kategori dan saran
    bmi = round(berat / (tinggi * tinggi),2)
    if bmi < 18.5:
        kategori = "Kurus"
        saran = "Makan yg banyak"
    elif bmi < 18.5:
        kategori = "Normal"
        saran = ""
    elif bmi < 25:
        kategori = "Gemuk"
        saran = "Kurangi Makan junkfood"
    else:
        kategori = "obesitas"
        saran = "Rawat"
            
    print(f"\nHalo {nama.capitalize()}, BMI Kamu Adalah {bmi}")
    print(f"Kategori : {kategori}")
    print(f"Saran : {saran}")
    
    lanjut = input("Mau Lajut (y/n) :")
    if lanjut != "y":
        break