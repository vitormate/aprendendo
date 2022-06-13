lista = [1, 2, 3, 4, 5]

print(lista)

indice = int(input(f'Digite o indice(de 0 até {len(lista)-1}) do elemento a ser removido: '))

'''
print(f'Elemento: {lista[indice]}')


lista_aux = []

for i in range(len(lista)):
    if i != indice:
        lista_aux.append(lista[i])

lista = lista_aux
'''

# A linha abaixo é equivalente ao bloco acima
print(f'Elemento: {lista.pop(indice)}')
# Se o metodo pop for usado sem nenhum número - x.pop() - ele removerá o ultimo elemento da lista.

print(lista)