m = int(input('Digite um número natural: '))
n = int(input('Digite outro número natural: '))

produto = max_x = max_y = 0
for x in range(m):
    for y in range(n):
        if (x*y - x**2 + y) > produto:
            produto = x*y - x**2 + y
            max_x = x
            max_y = y

print('')
print('Dada a expressão: x*y - x**2 + y')
print(f'O par ordenado que dá o valor máximo da expressão é {max_x, max_y} e o resultado da expressão é {produto}')
