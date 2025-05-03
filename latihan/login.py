#buat login sistem sederhana dengan whileloop
username = "admin"
password = 1234

maks_percobaan = 3

percobaan = 0
while percobaan < maks_percobaan:
    user = input("Masukkan Username :")
    pw = int(input("Masukkan Password :"))
    if user == username and pw == password:
        print("Berhasil Login")
        break
    else:
        percobaan += 1
        print("Username/Password Salah")
        print(f"Sisa Percobaan Login :{maks_percobaan - percobaan}")
        
if percobaan == maks_percobaan:
    print("Akun Anda Terkunci!")
    exit()