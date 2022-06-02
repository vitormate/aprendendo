from email.mime import base


num = int(input('Digite o valor da base: '))
expoente = int(input('Digite o expoente: '))
cont = 0
resultado = 1

while cont < expoente:
    resultado = resultado * num
    cont = cont + 1

print(num, 'elevado a', expoente, '=', resultado)
