#cara join set ada beberapa cara
# gunakan union() dan update() = menggabungkan semua item dari set
# interchange() = hanya menyimpan duplikat
#difference() = menyimpan item dari set pertama yang tidak ada di set lainnya.
#Metode symmetric_difference() menyimpan semua item KECUALI duplikat

#===== Union() =====
set1 = {1,2,3,4,5}
set2 = {"apple","banana","orange"}
set3 = set1.union(set2)
print(set3)

#===== update =====
et1 = {1,2,3,4,5}
set2 = {"apple","banana","orange"}
set1.update(set2)
print(set1)
#====intersection =====
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)