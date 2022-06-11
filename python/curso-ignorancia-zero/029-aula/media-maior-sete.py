alunos = 10

medias = []

for i in range(1, alunos+1):
    notas = 0
    for j in range(1, 4+1):
        notas += float(input(f'Digite a nota {j} de 4 do aluno {i} de {alunos}: '))
    notas /= 4

    medias.append(notas)

num = 0

for media in medias:
    if media >= 7:
        num += 1

print(f'O número de alunos com média maior do que 7 é {num}.')