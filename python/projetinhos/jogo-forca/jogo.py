# Jogo da Forca
import random

print(f'==========JOGO DA FORCA==========\n')

nome = input('Informe seu nome: ')

print(f'\nBoa sorte! {nome}')

lista = ['palavras', 'apenas', 'pequenas', 'vento']

x = random.choice(lista)

forca = []

for j in range(len(x)):
    forca.append('_')

turnos = 0
while turnos < 12:
    turnos += 1

    letra = input('\nTente uma letra: ')

    for i in range(len(x)):
        if letra == x[i]:
            forca.pop(i)
            forca.insert(i, letra)

    forca_tela = ' '.join(forca).upper()
    print(forca_tela)
    
    palavra = ''.join(forca)

    if x == palavra:
        break

if turnos <= 12:
    print(f'\nParabéns, {nome}! Você acertou a palavra em {turnos} chutes.')
else:
    print(f'\nMais sorte na próxima vez, {nome}! A palavra era {x}')
