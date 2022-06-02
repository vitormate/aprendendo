n = int(input('Digite um número: '))

aux, reverso = n, 0

while aux != 0:
    reverso = reverso*10 + aux%10
    aux //= 10

if reverso == n:
    print(f'{n} é palíndromo!')
else:
    print(f'{n} não é palíndromo!')
