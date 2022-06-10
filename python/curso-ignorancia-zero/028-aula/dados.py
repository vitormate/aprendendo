import random

vetor = []

n = int(input('Digite o número de lançamentos: '))
for i in range(n):
    vetor.append(random.randint(1, 6))

for i in range(1, 6+1):
    print(f'A face {i} ocorreu {(vetor.count(i) / n) * 100:.2f}% dos casos.')
