#menyimpan data dalam pasangan key:value
mahasiswa = {
    "nama" : "Irwan",
    "umur" : 31,
    "Jurusan" : "TI"
}
# print(mahasiswa["nama"])
for key, value in mahasiswa.items():
    print(f"{key}: {value}")
