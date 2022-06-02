p = int(input('Digite um número: '))
q = int(input('Digite maior ou igual ao anterior: '))

aux = p
cont = 0
while aux != 0:
    cont += 1
    aux = aux // 10

aux = q
temp = 0
while aux != 0:
    temp = aux % (10**cont) 

    if temp == p:
        aux = 0

    aux = aux // 10


print('')
if temp == p:
    print(f'p = {p}, q = {q}, p é subnúmero de q.')
else:
    print(f'p = {p}, q = {q}, p não é subnúmero de q.')
