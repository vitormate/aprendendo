import random

print('Olá, bem-vindo ao nosso programa! Vamos ver se você vai ganhar um carro ou não!\n')

porta_escolhida = int(input('Escolha uma porta: '))
#As próximas 3 linhas são equivalentes:
#premio = random.choice([1, 2, 3])
#premio = random.randrange(1, 4)
premio = random.randint(1, 3)

if 1 != premio and 1 != porta_escolhida:
    porta_aberta = 1
elif 2 != premio and 2 != porta_escolhida:
    porta_aberta = 2
elif 3 != premio and 3 != porta_escolhida:
    porta_aberta = 3

print(f'Você escolheu a porta {porta_escolhida}, mas eu lhe informo que na porta {porta_aberta} há um bode.')

trocar = int(input('Deseja trocar de porta? (1 - Sim/ 0 - Não): '))

if trocar == 1:
    if porta_escolhida != 1 and porta_aberta != 1:
        porta_escolhida = 1
    elif porta_escolhida != 2 and porta_aberta != 2:
        porta_escolhida = 2
    elif porta_escolhida != 3 and porta_aberta != 3:
        porta_escolhida = 3

if premio == porta_escolhida:
    print('Ganhou um carro!')
else:
    print('Ganhou um bode!')
