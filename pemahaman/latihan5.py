#latihan if else
#buat login dan percobaan 3x

#data login benar
username_benar = "admin"
password_benar = "1234"

#hitung jumlat percobaan
percobaan = 0
maks_percobaan = 3

while percobaan < maks_percobaan:
    username =input("Username :")
    password =input("Password :")
    if username_benar == username and password_benar == password_benar:
        print("Login Berhasil")
    else:
        percobaan += 1
        print("username atau password salah!")
        print(f"sisa percobaan : {maks_percobaan - percobaan}")
if maks_percobaan == percobaan:
    print("akun terkunci, silahkan coba lg nanti")
