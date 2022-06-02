n = int(input('Digite o comprimento da sequência: '))

ant = int(input('Digite o número 1: '))
seg = 1
cont = 1
while cont < n:
    prox = int(input(f'Digite o número {cont+1}: '))

    if prox != ant:
        seg += 1

    ant = prox
    cont += 1

print(f'A sequêcia tem {seg} segmentos')
