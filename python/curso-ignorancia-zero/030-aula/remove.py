n = int(input('Digite o número de elementos na lista: '))

lista = []
aux = []

for i in range(n):
    elemento = int(input(f'Digite o elemento {i+1} de {n}: '))
    lista.append(elemento)
    aux.append(elemento)

print(lista)

for ele in aux:
    apareceu = lista.count(ele)
    for i in range(apareceu-1):
        lista.remove(ele)

print(lista)
