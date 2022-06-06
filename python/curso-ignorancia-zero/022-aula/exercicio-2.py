num_maior = num_menor = aluno = int(input('Digite o número do 1 aluno: '))
menor = maior = altura = float(input('Digite a altura do 1 aluno: '))

for i in range(2, 10+1):
    aluno = int(input(f'Digite o número do {i} aluno: '))
    altura = float(input(f'Digite a altura do {i} aluno: '))

    if altura <= menor:
        menor = altura
        num_menor = aluno
    elif altura > maior:
        maior = altura
        num_maior = aluno

print(f'O aluno {num_maior} é o mais alto com {maior:.2f} metros.')
print(f'O aluno {num_menor} é o mais baixo com {menor:.2f} metros.')
