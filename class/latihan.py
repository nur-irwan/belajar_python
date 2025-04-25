class laptop:
    def __init__(self, merk , ram, ssd):
        self.merk = merk
        self.ram = ram
        self.ssd = ssd
    
    def spesifikasi(self):
        print("Laptop saya merk " + self.merk + " Ram " + self.ram + " penyimpanan " + self.ssd)
        
laptop1 = laptop("Axioo","8 GB", "500GB")
laptop1.spesifikasi()