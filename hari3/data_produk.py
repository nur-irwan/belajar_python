produk = {
            "P001" : {
                "nama" : "laptop",
                "harga" : 700000,
                "stok" : 10
            },
            "P002":{
                "nama" : "mouse",
                "harga" : 150000,
                "stok" : 30
            },
            "P003":{
                "nama" : "keyboard",
                "harga" : 250000,
                "stok" : 20
            }
        }
#cetak semua data produk
for kode, data in produk.items():
    print(f"{kode} - {data['nama']}| harga : {data['harga']}| stok : {data['stok']}")