n = int(input('Digite o número de sequências: '))
soma = 0
print('')
for i in range(n):
    num = int(input('Digite um número da sequência: '))

    if num % 2 == 0:
        soma += num
    
print(soma)
