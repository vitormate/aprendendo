turmas = int(input('Digite o número de turmas: '))

soma = 0
for i in range(1, turmas+1):
    alunos = int(input(f'Digite quantos alunos tem a turma {i}: '))

    while alunos > 40 or alunos < 0:
        print('Número de alunos inválido.')
        alunos = int(input(f'Digite quantos alunos tem a turma {i}: '))

    soma += alunos

print(f'A média de alunos por turma é {soma/turmas:.1f}')
