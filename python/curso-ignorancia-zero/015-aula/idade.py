n = int(input('Digite o número de pessoas: '))

cont = 0

while cont < n:
    dia = int(input(f'\nDigite o dia de nascimento da pessoa {cont + 1}: '))
    mes = int(input(f'Digite o mês de nascimento da pessoa {cont + 1}: '))
    ano = int(input(f'Digite o ano de nascimento da pessoa {cont + 1}: '))
    idade = int(input(f'Digite a idade a ser completada da pessoa {cont + 1}: '))

    print(f'A pessoa {cont + 1} fará {idade} anos no dia {dia}/{mes}/{ano+idade}')

    cont += 1
