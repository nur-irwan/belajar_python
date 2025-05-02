#Polimorphisom berarti satu interface tapi banyak bentuk
#ada 2 jenis polimorphisom
#1. Polymorphism via method override (dalam inheritance)
#2. Polymorphism via duck typing (tanpa inheritance, selama method-nya ada)

class Hewan:
    def suara(self):
        print("Hewan Bersuara")
class Kucing(Hewan):
    def suara(self):
        print("Meong")
        
class Ayam(Hewan):
    def suara(self):
        print("Kukuruyuk")
        
#pemakaian :
hewan1 = Kucing()
hewan2 = Ayam()

hewan1.suara()
hewan2.suara()

class Anjing(Hewan):
    def suara(self):
        print("Guk Guk Guk")
#Gabung semua objek ke dalam list
daftar_hewan = [Kucing(),Ayam(),Anjing()]
for hewan in daftar_hewan:
    hewan.suara()
    