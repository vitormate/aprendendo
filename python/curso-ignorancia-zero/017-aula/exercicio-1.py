eleitor = int(input('Digite o número de eleitores: '))
print('Digite 1 para votar no candidato A')
print('Digite 2 para votar no candidato B')
print('Digite 3 para votar no candidato C')

A = B = C = 0
for c in range(1, eleitor+1):
    voto = int(input('Vote: '))
    if voto == 1:
        A += 1
    elif voto == 2:
        B += 1
    elif voto == 3:
        C += 1

print(f'\nCadidato A teve {A} votos')
print(f'Cadidato B teve {B} votos')
print(f'Cadidato C teve {C} votos')
        