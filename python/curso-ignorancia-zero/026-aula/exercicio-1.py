notas = media = []
soma = 0
for i in range(4):
    nota = float(input(f'Nota {i+1}: '))
    notas.append(nota)
    soma += nota

media = soma / 4

print(f'Notas: {notas}')
print(f'Média: {media:.1f}')