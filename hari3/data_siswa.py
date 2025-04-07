#dictionary dalam dictionary atau nested dictionary
siswa = {
            "A001" : {
                "nama" : "ali",
                "umur" : 20,
                "jurusan" : "TI"
            },
            "A002" : {
                "nama" : "budi",
                "umur" : 21,
                "jurusan" : "SI"
            },
            "A003" : {
                "nama" : "Citra",
                "umur" : 22,
                "jurusan" : "MI"
            }
    }

print(siswa["A001"]["nama"])
print(siswa["A002"]["umur"])

#looping dictionary dalam dictionary
for nim, info in siswa.items():
    print(f"NIM:{nim}")
    print(f"nama : {info['nama']}")
    print(f"Umur : {info['umur']}")
    print(f"jurusan:{info['jurusan']}")