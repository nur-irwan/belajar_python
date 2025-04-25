class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        
    def info(self):
        print(f"{self.nama} adalah Hewan jenis {self.jenis}")
        
class Burung(Hewan):
    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi")
class Ikan(Hewan):
    def info(self):
        print(f"{self.nama} adalah Ikan air tawar")
        
elang = Burung("Elang", "Aves")
elang.info()
elang.terbang()

lele = Ikan("Lele", "Piesces")
lele.info()