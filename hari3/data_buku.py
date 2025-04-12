#dictionary dalam list
buku = [
    {
        "judul" : "python dasar",
        "penulis" : "budi",
        "tahun" : 2024
    },
    {
        "judul" : "ngoding santai",
        "penulis" : "budi",
        "tahun" : 2023
    },
    {
        "judul" : "data science 101",
        "penulis" : "citra",
        "tahun" : 2022
    }
]
for b in buku:
    print(f"{b['judul']} oleh {b['penulis']} ({b['tahun']})")