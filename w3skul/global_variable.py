# Create a variable outside of a function, and use it inside the function
#x = "awesome"

#def myFunc():
#    print("python is" + x)
    
#myFunc()
#===========================
#Create a variable inside a function, with the same name as the global variable
#x = "awesome"
#def myFunc():
#    x = "Fantastic"
#    print("Python is " + x)
#myFunc()
#print("Python is " + x)
#====================================
#If you use the global keyword, the variable belongs to the global scope:
#def myFunc():
#    global x
#    x = "fantastic"
#myFunc()

#print("python is " + x)
x = ["apple", "banana", "cherry"]
print(type(x))