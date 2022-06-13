lista = [1, 2, 3, 4, 5]

x = int(input('Digite o valor de x: '))
'''
achei = False
i = 0
while not achei and i < len(lista):
    if lista[i] == x:
        achei = True
        print(f'Elemento {x} se encontra no indice {i}')
    
    i+=1

if not achei:
    print(f'{x} não pertence a lista.')
'''

# O metodo index devolve o indice do elemento x.
print(lista.index(x))