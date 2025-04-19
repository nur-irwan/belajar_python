#program ubah detik ke jam:menit:detik

total_detik = int(input("Masukkan total Detik :"))

jam = total_detik // 3600
sisa = total_detik % 3600
menit = sisa // 60
detik = sisa %60
print(f"Waktu : {jam}:{menit}:{detik}")