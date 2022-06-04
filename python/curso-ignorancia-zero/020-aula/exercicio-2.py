a = float(input('Digite o valor de A: '))
if a == 0:
    print('Não existe equação de segundo grau com a = 0. Programa encerrado.')
else:
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))

    delta = b**2 - 4*a*c
    print('')
    if delta < 0:
        print(f'A equação não possui raízes reais, pois tem delta negativo: {delta}')
        print('Programa encerrado.')
    elif delta == 0:
        raiz = -b + (delta**(1/2)) / (2 * a)
        print(f'O delta é {delta}, então a função só possui uma raiz.')
        print(f'Raiz: {raiz}')
    else:
        raiz1 = (-b + (delta**(1/2))) / (2 * a)
        raiz2 = (-b - (delta**(1/2))) / (2 * a)
        print(f'O delta é positivo: {delta}, logo a equação possui duas raízes.')
        print(f'Raiz 1: {raiz1}')
        print(f'Raiz 2: {raiz2}')
