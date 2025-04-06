daftar_teman = [
    {
        "nama" : "elyana",
        "Kota" : "Medan",
        "Umur" : 33
    },
    {
        "nama" : "debby",
        "Kota" : "Bogor",
        "Umur" : 33
    },
    {
        "nama" : "Hardy",
        "Kota" : "Tangerang Selatan",
        "Umur" : 26
    }
]

for teman in daftar_teman:
    print(f"{teman['nama']} - dari {teman['Kota']} - {teman['Umur']} tahun")