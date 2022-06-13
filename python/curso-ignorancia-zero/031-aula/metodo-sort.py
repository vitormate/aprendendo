a = [5, 3, 1, 2, 4]
'''
aux = a[:]
b = []

while len(b) != len(a):
    menor = aux[0]
    for ele in aux:
        if ele < menor:
            menor = ele
    
    b.append(menor)
    aux.remove(menor)

a = b
'''

# O método sort vai organizar a lista em ordem crescente.
a.sort()
print(f'Lista = {a}')