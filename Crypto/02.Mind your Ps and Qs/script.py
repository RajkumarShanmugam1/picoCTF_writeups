#Given :
c = 964354128913912393938480857590969826308054462950561875638492039363373779803642185
n = 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
e = 65537

#Factors of n:
p = 2434792384523484381583634042478415057961
q = 650809615742055581459820253356987396346063
phi  = (p - 1) * (q - 1)

# Public Key
d = pow(e, -1, phi)
# Message in hex value
m = pow(c, d, n)
print(bytearray.fromhex(hex(m)[2:]).decode('ascii'))
