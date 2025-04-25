class Kendaraan:
    def __init__(self, merk):
        self.merk = merk
    def jalan(self):
        print(f"{self.merk} sedang berjalan")
class Motor(Kendaraan):
    def jenis(self):
        print(f"ini motor {self.merk}")
        
motor1 = Motor("Honda")
motor1.jalan()
motor1.jenis()

class Mobil(Kendaraan):
    def jalan(self):
        print(f"Mobil {self.merk} sedang melaju")
        
mobil1 = Mobil("Toyota")
mobil1.jalan()

        

