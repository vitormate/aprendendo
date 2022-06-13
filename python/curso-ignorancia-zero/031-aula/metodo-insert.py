a = [1, 2, 3, 4, 5]

print(f'Lista = {a}')

pos = int(input('Digite a posição: '))
ele = int(input('Digite o elemento: '))

'''
b = []

for i in range(len(a)):
    if i == pos:
        b.append(ele)
        
    b.append(a[i])

a = b

print(f'Lista = {a}')
'''

# O método insert serve para inserir um elemento na lista.
a.insert(pos, ele)

print(f'Lista = {a}')