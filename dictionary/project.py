#belajar dictionary
#buat dan ubah data karyawan
karyawan = {
    "nik" : 3211,
    "nama" : "dwi",
    "email" : "dwi@gmail.com",
    "no_tlp" : 85623132132
}
print(karyawan) #sebelum diubah
karyawan.update({"nama" : "irwan"})
karyawan.update({"nik" : 2200})
print(karyawan) #setelah diubah
karyawan.pop("no_tlp") #hapus item no_tlp
print(karyawan)