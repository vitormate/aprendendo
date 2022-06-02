n = int(input('Digite o valor de n: '))
fatorial = 1
for c in range(n, 1, -1):
    fatorial *= c

print(fatorial)
