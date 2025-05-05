#operator logika atau boolean

#not, or, and, xor
print("===NOT===")
a = True
c = not a
print('data a = ', a)
print('data a =', c)

#OR
print("===OR===")
a = True
b = False
c = a or b
print(a,'OR', b, '=', c)
a = False
b = True
c = a or b
print(a,'OR', b, '=', c)
a = False
b = False
c = a or b
print(a,'OR', b, '=', c)
a = True
b = True
c = a or b
print(a,'OR', b, '=', c)

#and
print("===and===")
a = True
b = False
c = a and b
print(a,'and', b, '=', c)
a = False
b = True
c = a and b
print(a,'and', b, '=', c)
a = False
b = False
c = a and b
print(a,'and', b, '=', c)
a = True
b = True
c = a and b
print(a,'and', b, '=', c)

#XOR
print("===XOR===")
a = True
b = False
c = a ^ b
print(a,'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a,'XOR', b, '=', c)
a = False
b = False
c = a ^ b
print(a,'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a,'XOR', b, '=', c)
