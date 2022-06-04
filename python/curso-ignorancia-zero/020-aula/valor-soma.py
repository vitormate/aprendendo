n = int(input('Digite um valor para n: '))
soma = 0.0
for i in range(1, n+1):
    soma = soma + i/(n - i + 1)

print(soma)
