# Obs.: Para esse programa era mais adequado usar o radom.uniform(a, b). Olhar documentação python.
import random

meu = [18, 19, 23, 28, 33, 48]

megasena = list(range(1, 61))

soma = 0

n = int(input('Número de testes: '))

for i in range(n):
    sorteado = []

    lista_premio = list(range(2, 71))
    premio = random.choice(lista_premio)
    premio_real = premio*10**6
    
    por_quina = random.choice([0.1, 0.2, 0.3, 0.4])

    deno_quadra = random.randint(5000, 30000)

    cont = quadra = quina = tudo = 0

    soma_ganho = soma_gasto = 0

    while cont < 50063860:
        soma_gasto -= 2.5

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
            soma_ganho += (premio_real * (1/deno_quadra))
        
        if len(aux) == 5:
            quina += 1
            soma_ganho += (premio_real * por_quina)
        
        if len(aux) == 6:
            tudo += 1
            soma_ganho += (premio_real * 0.94)
 
        cont += 1
        print(cont)
    soma += cont
    
    print(f'Resultado do teste {i}: {cont} tentativas para acertar todos os números.')
    print(f'Resultado do {i} teste: Você acertou {quina} quinas.')
    print(f'Resultado do {i} teste: Você acertou {quadra} quadras.')
    print(f'O total ganho foi: R$ {soma_ganho:.2f}')
    print(f'O total gasto foi: R$ {soma_gasto:.2f}')

soma /= n

print(f'Média dos resultados: {soma}')