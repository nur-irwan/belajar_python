class Hewan:
    def __init__(self, nama):
        self.nama = nama
        
    def makan(self):
        print(f"{self.nama} sedang makan")
        
class Kucing(Hewan):
    def suara(self):
            print(f"{self.nama} berkata meong")
            
kucing1 = Kucing("Amao")
kucing1.makan() #punya class hewan
kucing1.suara() #punya class kucing

#overiding atau mengganti sifat class parent
class Anjing(Hewan):
    def makan(self):
        print(f"{self.nama} makan tulang")
    def suara(self):
        print(f"{self.nama} menggongong : guk guk")
        
anjing1 = Anjing("Doggy")
anjing1.makan()
anjing1.suara()