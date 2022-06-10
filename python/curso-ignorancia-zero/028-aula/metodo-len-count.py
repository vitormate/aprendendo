lista = []
cont = 0
num = int(input('Digite um número da sequência: '))

while num != -1:
    lista.append(num)
    num = int(input('Digite um número da sequência: '))

elemento = int(input('Digite o elemento a ser procurado: '))

print(f'O elemento: {elemento} se repete {lista.count(elemento)} vezes na lista.')

for i in range(len(lista)):
    if lista[i] == elemento:
        cont += 1
    
print(f'O elemento: {elemento} se repete {cont} vezes na lista.')
