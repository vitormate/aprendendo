nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1+ nota2+ nota3) / 3
print('')
if media == 10:
    print('Aluno aprovado com distinção')
    print(f'Média: {media}')
elif media >= 7:
    print('Aprovado')
    print(f'Média: {media}')
elif media < 7:
    print('Reprovado')
    print(f'Média: {media}')
