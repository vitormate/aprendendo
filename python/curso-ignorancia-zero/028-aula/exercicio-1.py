vetor = []
jogadores = []
voto = 1


print('Enquete: Quem foi o melhor jogador?\n')

print('Informe um valor entre 1 e 23 ou 0 para sair!\n')


while voto != 0:
    voto = int(input('Número do jogador (0=fim): '))
    if voto > 0 and voto <= 23:
        vetor.append(voto)

print('\nResultado da votação: \n')

total_votos = len(vetor)
print(f'Foram computados {total_votos} votos.\n')

jogador_string = 'Jogador'
votos_string = 'Votos'
porcento_string = '%'

print(f'{jogador_string:^10} {votos_string:^10} {porcento_string:>8}')

for i in range(len(vetor)):
    if vetor[i] not in jogadores:
        jogadores.append(vetor[i])

num_votos = 0
for i in range(len(jogadores)):
    jogador = jogadores[i]
    votos = vetor.count(jogador)
    porcentagem = (votos / total_votos) * 100
    if num_votos < votos:
        melhor_jogador = jogador
        num_votos = votos
        total_porcentagem = porcentagem
    print(f'{jogador:^10} {votos:^10} {porcentagem:>10.1f}%')

print(f'O melhor jogador foi o número {melhor_jogador}, com {num_votos} votos, correspondendo a {total_porcentagem:.1f}% do total de votos.')
