a = [1,2,3,4,5]
b = [6,7,8,9,10]

print(a)

# O método clear limpa uma lista
a.clear()
print(a)

# O método copy cria uma cópia de outra lista, porém independente
# ou seja se umas das listas forem modificadas não afetará a outra.

# A linha abaixo é equivalente -> c = b[:]
c = b.copy()
print(c)