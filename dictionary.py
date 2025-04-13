# belajar dictionary
#customer = ["Irwan", 31, "Tangerang"] --> list
#buat dictionary
customer = {
    "nama": "Irwan",
    "age" : 31,
    "address" : "Tangerang"
    }
name = customer["nama"]
age = customer["age"]
address = customer["address"]


for key,value in customer.items():
    print(f"{key} : {value}")
    
