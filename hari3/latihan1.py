#buat fungsi sapa_lengkap(nama_Depan, nama_belakang)
#didalam nya, buat fungsi gabung_nama() yg menggabungkan dua nama, lalu print sapaan

def sapa_lengkap():
    def nama_depan():
        return "Irwan"
    def nama_belakang():
        return "nur"
    return f"Halo, {nama_depan()}{nama_belakang()}!"

#memanggil fungsi utama
print(sapa_lengkap())

    