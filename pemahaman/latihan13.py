#program atm sederhana
from datetime import datetime
pin_benar = "1234"
percobaan = 0
maks_percobaan = 3
saldo = 5000000
riwayat = []

#login atm
while percobaan < maks_percobaan:
    pin = input("Masukkan PIN :")
    if pin == pin_benar:
        print("login berhasil")
        while True:
            print("\n=== MENU ATM ===")
            print("1. Cek Saldo")
            print("2. Setor Uang")
            print("3. Tarik Tunai")
            print("4. Riwayat")
            print("5. Keluar")
            menu = input("Pilih menu (1/2/3/4/5): ")
            if menu == "1":
                print(f"Saldo anda adalah Rp.{saldo:,}")
            elif menu == "2":
                setor = int(input("Masukkan Jumlah yg Akan Di Setor :"))
                saldo += setor
                waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
                riwayat.append(f"{waktu} - Setor: Rp.{setor:,}")
                print(f"Setor Berhasil, Saldo Anda Rp.{saldo:,}")
                with open("transaksi_atm.txt", "a") as file:
                    file.write(f"{waktu}, Setor : Rp.{setor:,}\n")
            elif menu == "3" :
                tarik_tunai = int(input("Masukkan Nominal : Rp."))
                if tarik_tunai > saldo:
                    print("Saldo Tidak Cukup")
                else:
                    saldo -= tarik_tunai
                    waktu = datetime.now().strftime("%d/%m/%Y %H:%M")
                    riwayat.append(f"{waktu} - Tarik Tunai: Rp.{tarik_tunai:,}")
                    print(f"Tarik Tunai Berhasil, Sisa Saldo Rp.{saldo:,}")
                    with open("transaksi_atm.txt", "a") as file:
                        file.write(f"{waktu}, Tarik Tunai : Rp.{tarik_tunai:,}\n")
            elif menu == "4":
                print("===Riwayat Transaksi===")
                if len(riwayat) == 0:
                    print("Belum Ada Transaksi")
                else:
                    for r in riwayat:
                        print("-", r)
            elif menu == "5":
                print("Terima Kasih Sudah Menggunakan ATM")
                break
            else:
                print("Menu Tidak Valid")
        break
    else:
        percobaan += 1
        print("PIN Salah")
        print(f"Sisa Login {maks_percobaan - percobaan}")
if percobaan == maks_percobaan:
    print("ATM diblokirs")
    exit()