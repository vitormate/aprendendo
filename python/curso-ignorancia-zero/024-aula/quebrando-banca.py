import random

testes = int(input('Digite o número de testes: '))

trocar = 0
n_trocar = 0

for i in range(testes):
    porta = random.randrange(1, 4)
    premio = random.randint(1, 3)

    if porta == premio:
        n_trocar += 1
    else:
        trocar += 1

print(f'É vantajoso trocar em {trocar*100/testes:.1f} % das vezes')
print(f'Não é vantajoso trocar em {n_trocar*100/testes:.1f} % das vezes')
