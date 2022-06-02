saque = int(input('Digite o valor do saque: '))

if saque < 10:
    print('Valor abaixo do saque mínimo, saque NEGADO.')
if saque > 600:
    print('Valor acima do saque máximo, saque NEGADO.')

if 10 <= saque <= 600:

    cedulas_100 = saque // 100
    saque = saque % 100

    cedulas_50 = saque // 50
    saque = saque % 50

    cedulas_10 = saque // 10
    saque = saque % 10

    cedulas_5 = saque // 5
    saque = saque % 5

    cedulas_1 = saque // 1

    if cedulas_100 > 0:
        print(cedulas_100, 'nota(s) de R$ 100,00')
    if cedulas_50 > 0:
        print(cedulas_50, 'nota(s) de R$ 50,00')
    if cedulas_10 > 0:
        print(cedulas_10, 'nota(s) de R$ 10,00')
    if cedulas_5 > 0:
        print(cedulas_5, 'nota(s) de R$ 5,00')
    if cedulas_1 > 0:
        print(cedulas_1, 'nota(s) de R$ 1,00')
        