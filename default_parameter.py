#belajar default argument value

def say_hello(first_name="irwan", last_name=""):
    print(f"Hello{first_name} {last_name}")
    
say_hello("Dwi")
say_hello(last_name="agustina")