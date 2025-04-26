class Mahasiswa:
    def __init__(self, nama, nilai):
        self.nama = nama #public
        self._jurusan = "TI" #protected
        self.__nilai = nilai #private
        
    def tampilkan_nilai(self):
        print(f"{self.nama} Memiliki Nilai {self.__nilai}")
        
    def ubah_nilai(self, nilai_baru):
        if 0 <= nilai_baru <= 100:
            self.__nilai = nilai_baru
        else :
            print("Nilai Harus antara 0 dan 100")
mhs1 = Mahasiswa("Irwan", 80)
mhs1.tampilkan_nilai() #bisa
mhs1.ubah_nilai(95) #bisa
print(mhs1.nama) #public = bisa
print(mhs1._jurusan) #bisa, tapi tidak disarankan (protected)
print(mhs1._Mahasiswa__nilai) #akses private
