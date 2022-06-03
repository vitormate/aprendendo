i = int(input('Digite um valor para i: '))
j = int(input('Digite um valor para j: '))

print(f'Os divisores comuns de {i} e {j} são: ')
print(1)
divisor = 2
while divisor <= i and divisor <= j:
    if i % divisor == 0 and j % divisor == 0:
        print(divisor)
    divisor += 1
