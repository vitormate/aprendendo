n = int(input('Digite o tamanho da sequência: '))

ant = int(input('Digite o 1 número: '))
prox = 0
seg = 1
segMAX = 1

cont = 1

while cont < n:
    prox = int(input(f'Digite o {cont+1} número: '))

    if prox > ant:
        seg += 1
    else:
        if seg > segMAX:
            segMAX = seg
        seg = 1

    cont += 1
    ant = prox

print(f'O maior segmento crescente da sequência é: {segMAX}')
