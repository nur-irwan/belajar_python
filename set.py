#belajar set
#data harus unique
#posisi index bisa berubah-ubah
#list = []
#tuple = ()
#set = {}

nama = {"irwan","dwi","agustina","nur","dwi"}

nama.add("iwang")
nama.add("iwang")
nama.add("iwang")

for data in nama:
    print(data)
nama.remove("nur")
print(nama)
