n = int(input('Digite um número: '))

aux = str(n)
dig = ''
reverso = ''

c = 0
final = len(aux)

while c < final:
    dig = aux[-1]

    reverso = reverso + dig

    aux = aux[:len(aux)-1]
    
    c += 1

reverso = int(reverso)

if n == reverso:
    print(f'O número {n} é palindromo!')
else:
    print(f'O número {n} não é palindromo!')
