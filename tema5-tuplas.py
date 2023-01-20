tupla = (1,2,3)
print(tupla)
print(type(tupla))

tupla2 = (7, "Roberto", True, 23.8, 16+7)
print(tupla2)
print(tupla2[1])
print(tupla2[0:3])

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaN = tupla + tupla2
print(tuplaN)

print(tupla.count(2))

tupla[2] = 23
