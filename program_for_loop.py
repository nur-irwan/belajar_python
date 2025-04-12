#membuat program mengggunakan for-loop, list dan range

banyak = int(input("Berapa banyak data?"))
nama = []
umur = []
for i in range(0, banyak):
    print(f"data ke {i}")
    input_nama = input("Nama :")
    input_umur = int(input("Umur :"))
    
    nama.append(input_nama)
    umur.append(input_umur)
    
for a in range(0, len(nama)):
    data_nama = nama[a]
    data_umur = umur[a]
    print(f"{data_nama} berumur {data_umur} tahun")