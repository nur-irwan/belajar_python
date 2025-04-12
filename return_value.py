#belajar method return value

def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"Total {list_angka} = {total}")
    return total

total = jumlahkan(10,5,20,5)
#mengambil data total
print(total)