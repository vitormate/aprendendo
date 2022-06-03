lado1 = int(input('Digite um número: '))
lado2 = int(input('Digite outro número: '))
lado3 = int(input('Digite mais um número: '))

if lado1**2 + lado2**2 == lado3**2 or lado1**2 + lado3**2 == lado2**2 or lado2**2 + lado3**2 == lado1**2:
    print('Esses números formam um triângulo retângulo!')
else:
    print('Esse números não formam um triângulo retângulo.')
