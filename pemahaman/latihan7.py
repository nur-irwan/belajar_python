#program cek berat badan ideal
tinggi = int(input("Masukkan Tinggi Badan (cm):"))
berat = int(input("Masukkan Berat badan (kg) :"))

Berat_ideal = (tinggi - 100) - ((tinggi - 100) * 0.1)

if berat < Berat_ideal:
    print("Badan kurang ideal")
elif berat > Berat_ideal:
    print("berat badan berlebih")
else:
    print("badan ideal")

