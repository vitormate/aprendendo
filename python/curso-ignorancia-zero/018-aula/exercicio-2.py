# Não consegui compreender esse exercício.
m = int(input('Digite um número: '))

for n in range(1, m+1):
    soma, inicio = 0, 1
    while soma != n**3:
        soma = 0
        for i in range(n):
            soma = soma + inicio + 2 * i
        inicio += 2

    inicio = inicio - 2
    print(f'{n}*{n}*{n} = {n**3}')
    for i in range(n):
        print('+', inicio+2*i)
    print('\n')