# Jogo de Adivinhação de Números
import random
import math

inicio = int(input('Digite o início do intervalo: '))
fim = int(input('Digite o fim do intervalo: '))

n_aleatorio = random.randint(inicio, fim)
print(n_aleatorio)
chances = round(math.log(fim - inicio + 1, 2))
print(f'Você tem apenas {chances} chances para adivinhar o número!')

cont = 0
while cont < chances:
    cont += 1

    chute = int(input('\nTente adivinhar o número escolhido pelo PC: '))
    
    if chute > n_aleatorio:
        print('Tente novamente! Você adivinhou muito alto.')
    elif chute < n_aleatorio:
        print('Tente novamente! Você adivinhou muito pequeno.')
    else:
        print(f'\nParabéns! Você acertou em {cont} tentativas')
        break    

if cont >= chances:
    print(f'\nO número era {n_aleatorio}')
    print('Melhor sorte na próxima vez!')
