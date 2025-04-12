#dictionary dalam list
mahasiswa = [
    {
        "nama": "ali",
        "umur" : 20,
        "jurusan" : "TI"
    },
    {
        "nama" : "budi",
        "umur" : 22,
        "jurusan" : "SI"
    },
    {
        "nama" : "Citra",
        "umur" : 21,
        "jurusan" : "MI"
    }
]
for mhs in mahasiswa : 
    print(f"{mhs['nama']} - {mhs['umur']} tahun - Jurusan :{mhs['jurusan']}")