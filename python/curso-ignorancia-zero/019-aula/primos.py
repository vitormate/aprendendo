n = int(input('Digite um número: '))
div = 0
for i in range(1, n+1):
    primo = True
    j = 2
    while j < i and primo:
        div += 1
        if i % j == 0:
            primo = False
        j += 1
    
    if primo:
        print(f'{i} é primo')
print(f'Fiz {div} divisões.')
