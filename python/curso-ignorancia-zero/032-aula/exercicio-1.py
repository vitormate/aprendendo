import random

megasena = list(range(1, 61))

soma = 0

n = int(input('Número de testes: '))

for t in range(n):
    meu = []

    mega_aux = megasena.copy()

    for i in range(6):
        seu_num = random.choice(mega_aux)
        meu.append(seu_num)
        mega_aux.remove(seu_num)
    
    meu.sort()

    sorteado = []

    cont = 0


    while meu != sorteado:
        meu.clear()

        mega_aux = megasena.copy()

        for i in range(6):
            seu_num = random.choice(mega_aux)
            meu.append(seu_num)
            mega_aux.remove(seu_num)
        
        meu.sort()


        mega_sort = megasena.copy()

        sorteado = []

        for j in range(6):
            num_sorteado = random.choice(mega_sort)
            sorteado.append(num_sorteado)
            mega_sort.remove(num_sorteado)
        
        sorteado.sort()

        cont += 1
        print(cont)
    
    soma += cont
    
    print(f'Resultado do teste {t}: {cont} tentativas.')

    print(meu, sorteado)

soma /= n

print(f'Média dos resultados: {soma}')