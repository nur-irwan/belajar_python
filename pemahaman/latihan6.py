#program untuk menghitung gaji akhir karyawan berdasarkan status kerja

status = input("Status : (tetap/kontrak):")
gaji_pokok = int(input("Masukkan Gaji pokok :"))
#tambahn tunjangan untuk karyawan tetap
if status.lower() == "tetap":
    tunjangan = 0.2 * gaji_pokok
else :
    tunjangan = 0
    
gaji_total = gaji_pokok + tunjangan
print(f"Gaji Total : {gaji_total}")