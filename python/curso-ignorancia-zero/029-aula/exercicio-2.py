lista = []
num = 0

while num != -1:
    num = float(input('Digite um número: '))

    lista.append(num)

print("Os seguintes números da lista são pares: ")
for i in lista:
    if i % 2 == 0:
        print(i)
