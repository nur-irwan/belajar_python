#looping pada pada dictionary python
thisdict = {
    "nama" : "irwan",
    "umur" : 31,
    "jenis_kelamin" : "laki-laki"
}
#for x in thisdict:
    #print(x) #cetak items
    #print(thisdict[x]) #cetak value
    
for x,y in thisdict.items():
    print(x,y)