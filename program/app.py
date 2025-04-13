#membuat program management kontak
import function
#list of dictionary
daftar_kontak = []
daftar_kontak.append({
    "nama" : "Irwan",
    "email" : "nurirwan@gmail.com",
    "telepon" : "089232342344"
})
# menu program
while True:
    print("# menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. keluar program")
    
    menu = input("pilih menu :")
    
    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("menu tidak tersedia")
    
print("program selesai berjalan, sampai jumpa")
    
