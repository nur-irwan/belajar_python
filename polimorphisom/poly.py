class Manusia:
    def identitas(self):
        print("Saya manusia biasa.")

class Robot:
    def identitas(self):
        print("Saya robot generasi ke-9.")

class Alien:
    def identitas(self):
        print("Saya alien dari planet Xorx.")

def perkenalan(makhluk):
    makhluk.identitas()  # Duck typing: asal punya method identitas()

# Pemakaian
daftar_objek = [Manusia(), Robot(), Alien()]

for makhluk in daftar_objek:
    perkenalan(makhluk)
