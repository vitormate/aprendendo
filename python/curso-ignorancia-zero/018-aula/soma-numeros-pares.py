n = int(input('Digite o número de sequências: '))

print('')
for i in range(n):
    print(f'Sequência: {i+1}')
    num = int(input('Digite um número da sequência: '))
    soma = 0

    while num != 0:
        if num % 2 == 0:
            soma += num
        num = int(input('Digite um número da sequência: '))
    
    print(f'A soma da sequência {i+1} é {soma}')
    print('')
