num = int(input('Digite um número inteiro não negativo: '))
resultado = 1
cont = num

while cont > 1:
    resultado = resultado * cont
    cont = cont - 1

print(num, '! =', resultado)
