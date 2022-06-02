n = int(input('Digite um número: '))

cont, soma = 2, 1

while cont < n:
    if n % cont == 0:
        soma += cont
    cont += 1

if soma == n:
    print(f'O número {n} é perfeito')
else:
    print(f'O número {n} não é perfeito')
