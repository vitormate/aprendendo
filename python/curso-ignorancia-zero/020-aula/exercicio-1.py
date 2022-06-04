altura = float(input('Digite a altura da pessoa: '))
sexo = int(input('Digite o sexo da pessoa 0/1(masculino/feminino): '))
peso = float(input('Digite o peso da pessoa: '))

if sexo == 0:
    imc = (72.7 * altura) - 58
elif sexo == 1:
    imc = (62.1 * altura) - 44.7

if peso > imc:
    print('A pessoa está acima do peso.')
    print(f'Peso atual: {peso}')
    print(f'Peso ideal: {imc}')
elif peso < imc:
    print('A pessoa está abaixo do peso.')
    print(f'Peso atual: {peso}')
    print(f'Peso ideal: {imc}')
else:
    print('A pessoa está dentro do peso ideal.')
    print(f'Peso atual: {peso}')
    print(f'Peso ideal: {imc}')
