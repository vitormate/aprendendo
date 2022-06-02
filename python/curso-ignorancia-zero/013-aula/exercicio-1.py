n = int(input('Digite um número: '))
resultado = 0
cont = 1

if n > 0:
    while cont <= n:
        num = int(input('Digite um número da sequência: '))
        if num > 0:
            resultado = resultado + num
        cont = cont + 1

    print('Resultado: ', resultado)

else:
    print(n, 'não é um número válido para esse programa')
