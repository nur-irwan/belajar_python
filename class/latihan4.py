#Buat class AkunBank dengan atribut:
#__nama (private)
#__saldo (private)

#Buat method:
#tampil_info() → cetak nama dan saldo
#setor(uang) → menambah saldo
#tarik(uang) → mengurangi saldo jika cukup, kalau tidak, tampilkan pesan “Saldo tidak cukup!”

class AkunBank:
    def __init__(self, nama, saldo):
        self.__nama = nama  # private
        self.__saldo = saldo  # private
        
    def tampil_info(self):
        print(f"Nama Akun Anda: {self.__nama}, Saldo Anda: Rp{self.__saldo}")
    
    def setor(self, uang):
        if uang > 0:
            self.__saldo += uang
            print(f"Berhasil setor Rp{uang}")
        else:
            print("Jumlah setor tidak valid")
    
    def tarik(self, uang):
        if uang > self.__saldo:
            print("Saldo tidak cukup!")
        else:
            self.__saldo -= uang
            print(f"Berhasil tarik tunai Rp{uang}")

# Penggunaan
akun1 = AkunBank("Irwan", 100000)
akun1.setor(10000)
akun1.tarik(5000)
akun1.tampil_info()

            

            