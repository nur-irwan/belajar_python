#membuat data siswa
#==============fitur================
#1. menampilkan semua data siswa
#2. menambahkan data siswa
#3. mencari nilai siswa berdasarkan nama
#4. keluar dari program

siswa = {}

while True:
    print("\n=======Menu Data Siswa===========")
    print("1. Tampilkan Semua data")
    print("2. tambah data siswa")
    print("3. cari nilai siswa")
    print("4. Keluar")
    
    pilih = input("Pilih Menu (1/2/3/4) :")
    if pilih == "1":
        if not siswa:
            print("belum ada data siswa")
        else:
            print("\nData Siswa:")
            for nama,nilai in siswa.items():
                print(f"- {nama}: {nilai}")
    elif pilih == "2":
        nama = input("Masukkan Nama Siswa :")
        nilai = int(input("Masukkan nilai Siswa : "))
        siswa[nama] = nilai
        print(f"Data untuk {nama} telah ditambahkan")
    elif pilih == "3":
        nama = input("Input Nama Siswa yg di cari:")
        if nama in siswa:
            print(f"Nilai {nama} adalah {siswa[nama]}")
        else:
            print(f"{nama} tidak di temukan dalam data")
    elif pilih == "4":
        print ("Keluar dari program.Terima kasih")
        break
    else:
        print("Pilihan tidak valid.")