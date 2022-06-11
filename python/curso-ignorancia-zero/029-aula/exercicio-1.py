lista = []
elemento = 0

while elemento != -1:
    elemento = float(input('Digite um número: '))
    lista.append(elemento)

print("Os seguintes números da lista são maiores do que 10")
for num in lista:
    if num > 10:
        print(num)