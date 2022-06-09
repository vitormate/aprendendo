par = []
impar = []

for i in range(20):
    num = int(input(f'Digite o {i+1}º número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'\nVetor par: {par}\n')
print(f'Vetor ímpar: {impar}')