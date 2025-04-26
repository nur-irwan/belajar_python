class PemainBola:
    def __init__(self, nama, posisi):
        self.__nama = nama
        self.__posisi = posisi
        
    def tampil_info(self):
        print(f"{self.__nama}, posisi:{self.__posisi}")
        
    def ubah_posisi(self, posisi_baru):
        if self.__posisi:
            self.__posisi = posisi_baru
            print(f"posisi pemain {self.__nama} telah diubah menjadi {self.__posisi} ")

pemain = PemainBola("Irwan", "Penyerang")
pemain.tampil_info()
pemain.ubah_posisi("Gelandang")
pemain.tampil_info()