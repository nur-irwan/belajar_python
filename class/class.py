class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna
    def info(self):
        print(f"Mobil {self.merk} bewarna {self.warna}")
        
mobil1 = Mobil("toyota", "merah")
mobil2 = Mobil("honda", "apa aja yg penting dibayarin")


mobil1.info()
print(mobil1.warna)
mobil2.info()