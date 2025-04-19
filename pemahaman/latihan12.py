pin = "1234"
saldo_atm = {
    "saldo": 5000000
}

while True:
    login = input("Masukkan PIN login: ")
    if login == pin:
        print("Login berhasil!\n")
        
        while True:
            print("\n=== MENU ATM ===")
            print("1. Cek Saldo")
            print("2. Setor Uang")
            print("3. Tarik Tunai")
            print("4. Keluar")
            
            menu = input("Pilih menu (1/2/3/4): ")
            
            if menu == "1":
                print("Saldo anda adalah Rp.", saldo_atm["saldo"])
            elif menu == "2":
                setor = int(input("Masukkan jumlah setor: "))
                saldo_atm["saldo"] += setor
                print("Setor berhasil. Saldo sekarang: Rp.", saldo_atm["saldo"])
            elif menu == "3":
                tarik = int(input("Masukkan jumlah tarik: "))
                if tarik > saldo_atm["saldo"]:
                    print("Saldo tidak cukup!")
                else:
                    saldo_atm["saldo"] -= tarik
                    print("Penarikan berhasil. Saldo sekarang: Rp.", saldo_atm["saldo"])
            elif menu == "4":
                print("Terima kasih telah menggunakan ATM.")
                break
            else:
                print("Menu tidak valid!")

        break  # keluar dari loop login setelah selesai
    else:
        print("PIN salah. Akses ditolak.")
        break
