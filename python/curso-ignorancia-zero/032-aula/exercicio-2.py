import random

meu = [18, 19, 23, 28, 33, 48]

megasena = list(range(1, 61))

soma = 0

n = int(input('Número de testes: '))

for i in range(n):
    sorteado = []

    cont = quadra = quina = 0

    while meu != sorteado:
        mega_sort = megasena.copy()
    
        aux = []

        sorteado = []

        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)
        
        sorteado.sort()

        for x in range(6):
            num = sorteado[x]
            for y in range(6):
                if num == meu[y]:
                    aux.append(num)
        
        if len(aux) == 4:
            quadra += 1
        
        if len(aux) == 5:
            quina += 1
        
        cont += 1
    
    soma += cont
    
    print(f'Resultado do teste {i+1}: {cont} tentativas para acertar todos os números.')
    print(f'Resultado do {i} teste: Você acertou {quina} quinas.')
    print(f'Resultado do {i} teste: Você acertou {quadra} quadras.')

soma /= n

print(f'Média dos resultados: {soma}')