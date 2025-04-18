#membuat function 
def my_function():
    print("Hello from a function")
my_function()

def panggil(fname):
    print(fname + "Irwan")
    
panggil("Nur")

def namalengkap(fname, lname):
    print(fname + "  " + lname)
namalengkap("Nur" , "Irwan")

def namaLengkap(*kids):
    print("The Youngest child is "+ kids[2])
namaLengkap("irwan","dwi","agustina")

#default parameter value
def my_function(country = "Indonesia"):
    print("I am From" + country)
my_function("sweden")
my_function("india")
my_function("china")

# return value
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))