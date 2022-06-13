vetor = []

loop = True

while loop:
    nota = float(input('Digite uma nota ou -1 para sair: '))
    vetor.append(nota)

    if nota == -1:
        loop = False

vetor.remove(-1)

notas = len(vetor)

print(f'Foram lidas {notas} notas.')

print(vetor)

vetor.reverse()
print(vetor)

soma = 0
for elemento in vetor:
    soma += elemento

print(f'A soma de todas as notas {soma}')

media = soma / notas

print(f'A média das notas é: {media:.1f}')

acima_media = abaixo_sete = 0
for elemento in vetor:
    if elemento > media:
        acima_media += 1
    if elemento < 7:
        abaixo_sete += 1


print(f'{acima_media} nota(s) estão acima da média.')
print(f'{abaixo_sete} nota(s) estão abaixo de sete.')

print('\nFim do Programa!')