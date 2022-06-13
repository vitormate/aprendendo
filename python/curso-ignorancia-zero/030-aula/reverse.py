idades = []
alturas = []

for i in range(1, 5+1):
    idade = int(input(f'Digite a idade da {i} pessoa: '))
    altura = float(input(f'Digite a altura da {i} pessoa: '))

    idades.append(idade)
    alturas.append(altura)

# Os três blocos abaixo são equivalentes

'''
idades_invertida = idades[::-1]
alturas_invertida = alturas[::-1]

for i in range(5):
    print(f'Idade {5 - i}: {idades_invertida[i]}')
    print(f'Altura {5 - i}: {alturas_invertida[i]}')
'''

'''
for i in range(4, -1, -1):
    print(f'Idade {i+1}: {idades[i]}')
    print(f'Altura {i+1}: {alturas[i]}')
'''

idades.reverse()
alturas.reverse()

for i in range(5):
    print(f'Idade {5 - i}: {idades[i]}')
    print(f'Altura {5 - i}: {alturas[i]}')