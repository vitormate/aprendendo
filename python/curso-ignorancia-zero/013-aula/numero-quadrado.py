num = int(input('Digite o primeiro número: '))
resultado = 0

while num != 0:
    resultado = num**2
    print(num, 'ao quadrado =', resultado)
    num = int(input('Digite o próximo número: '))
