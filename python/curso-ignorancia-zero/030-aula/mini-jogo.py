import random

player_vida = 500
player_sp = 100

inimigo_vida = 50

n = int(input('Digite o número de inimigos: '))

inimigos = []

for i in range(n):
    inimigos.append([i+1, inimigo_vida])

jogando = True
while jogando:
    print(f'Vida: {player_vida}')
    print(f'SP: {player_sp}')

    escolha = int(input('Deseja atacar (1) ou curar (2): '))
    
    if escolha == 1:
        inimigo_escolhido = random.choice(inimigos)
        dano = random.randint(10, 15)
        print(f'Causou {dano} de dano ao inimigo {inimigo_escolhido[0]}!')

        inimigo_escolhido[1] -= dano

        if inimigo_escolhido[1] <= 0:
            print(f'Inimigo {inimigo_escolhido[0]} morreu!')
            inimigos.remove(inimigo_escolhido)

    else:
        if player_sp > 10:
            cura = random.randint(10, 15)
            print(f'Você recebeu {cura} de vida!')

            player_vida += cura
            player_sp -= 10
        
        else:
            print('SP insuficiente!')

    for inimigo in inimigos:
        acertou = bool(random.choice([1, 1, 1, 0]))

        if acertou:
            dano_inimigo = random.randint(1, 3)
            print(f'Inimigo {inimigo[0]} causou {dano_inimigo} de dano!')
            player_vida -= dano_inimigo
        else:
            print(f'Inimigo {inimigo[0]} errou o ataque!')
            


    if player_sp < 100:
        player_sp += 3
    
    if player_sp > 100:
        player_sp = 100

    if player_vida <= 0:
        print('Perdeu o jogo!')
        jogando = False

    if len(inimigos) == 0:
        print('Ganhou o jogo!')
        jogando = False