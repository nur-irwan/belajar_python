class RekeningBank:
    def __init__(self, nama, saldo):
        self.__nama = nama
        self.__saldo = saldo
        
    def tampil_info(self):
        print(f"Nama Pemilik Rekening {self.__nama}, Jumlah saldo {self.__saldo}")
    
    def setor(self, uang):
        if uang > 0:
            self.__saldo += uang
            print(f"Anda Berhasil Setor sebanyak Rp.{uang}, Saldo Anda {self.__saldo}")
        else :
            print("jumlah setor tidak valid")
    def tarik(self, uang):
        if uang > self.__saldo:
            print("saldo tidak cukup")
        else:
            self.__saldo -= uang
            print(f"Anda Berhasil Tarik Uang sejumlah {uang}, saldo anda sisa {self.__saldo}")
            self.__cek_saldo_minimum()

    def __cek_saldo_minimum(self):
        if self.__saldo <= 50000:
            print("Saldo Anda Dibawah Minumum, segera lakukan penyetoran")
            
rekening = RekeningBank("Irwan", 100000)
rekening.setor(50000)
rekening.tampil_info()
rekening.tarik(100000)
rekening.tampil_info()
