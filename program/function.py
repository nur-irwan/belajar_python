#management kontak program

def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("==============")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"No tlp : {kontak['telepon']}")
        
def new_kontak():
    nama = input("nama :")
    email = input("email :")
    telepon = input("telepon :")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak 

def hapus_kontak(daftar_kontak):
    telepon = input("No telepon yang akan di hapus : ")
    index = -1
    
    for i in range(0,len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break
    if index == -1:
        print("data tidak di temukan")
    else:
        del daftar_kontak[index]
        print("telepon berhasil dihapus")
        
def cari_kontak(daftar_kontak):
    nama_cari = input("Nama yg akan di cari :")
    
    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_cari.lower()) != -1:
            print("==============")
            print(f"Nama : {kontak['nama']}")
            print(f"Email : {kontak['email']}")
            print(f"No tlp : {kontak['telepon']}")
    