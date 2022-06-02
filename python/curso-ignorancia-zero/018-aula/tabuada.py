comeco = int(input('Começo = '))
fim = int(input('Fim = '))

for i in range(comeco, fim+1):
    print(f'\nPara o {i}:')
    for j in range(comeco, fim+1):
        print(f'{i}X{j} = {i*j}')
