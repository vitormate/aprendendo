num = int(input('Digite um número para verificar se ele é triangular: '))

a = 1

print('')
while a * (a + 1) * (a + 2) < num:
    print(a, 'X', a + 1, 'X', a + 2, '=', a*(a+1)*(a+2))
    a += 1


print('')
if a * (a + 1) * (a + 2) == num:
    print(num, 'é triangular, pois', a, '.', a + 1, '.', a + 2, '=', a*(a+1)*(a+2))
else:
    print(num, 'não é triangular, pois', a, '.', a + 1, '.', a + 2, '=', a*(a+1)*(a+2))
