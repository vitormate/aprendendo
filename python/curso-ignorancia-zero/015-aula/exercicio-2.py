n = int(input('Digite a quantidade de número a ser digitada: '))

cont = 0
soma = 0

while cont < n:
    num = int(input(f'Digite o {cont+1}° número: '))

    if num % 2 == 0:
        soma += num
    
    cont += 1

print(f'A soma dos números pares é: {soma}')

