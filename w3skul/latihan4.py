#membuat kalkulator sederhana
angka1 = float(input("Masukkan Angka Pertama :"))
angka2 = float(input("Masukkkan angka kedua :"))

print("Pilih operator: +-*/")
operasi = input("masukkan operasi: ")
if operasi == "+":
    hasil = angka1 + angka2
elif operasi == "-":
    hasil = angka1 - angka2
elif operasi == "*":
    hasil = angka1 * angka2
elif operasi == "/":
    hasil = angka1 / angka2
else:
    hasil = "Operasi tidak dikenali"
    
print("Hasil : ",hasil)