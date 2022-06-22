# Jogo da Forca
import random

print(f'==========JOGO DA FORCA==========\n')

nome = input('Informe seu nome: ')

print(f'\nBoa sorte! {nome}')

lista = ['palavras', 'apenas', 'pequenas', 'vento']

x = random.choice(lista)
tamanho = len(x)

forca = []
letras = []

for j in range(len(x)):
    forca.append('*')

print(f'\nA palavra tem {tamanho} letras')

turnos = 12
while turnos != 0:
    print(f'Você tem {turnos} chances')

    letra = input('\nTente uma letra: ')
    
    while letra in letras:
        letra = input('\nTente uma letra: ')
    
    letras.append(letra)

    for i in range(len(x)):
        if letra == x[i]:
            forca.pop(i)
            forca.insert(i, letra)

    forca_tela = ' '.join(forca).upper()
    print(forca_tela)
    
    palavra = ''.join(forca)

    if x == palavra:
        print(f'\nParabéns, {nome}! Você acertou a palavra.')
        break
    
    turnos -= 1

if x != palavra:
    print(f'\nMais sorte na próxima vez, {nome}! A palavra era {x}')
