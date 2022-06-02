a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a >= b >= c:
    print(a, 'é o maior número')
    print(c, 'é o menor número')
elif a >= c >= b:
    print(a, 'é o maior número')
    print(b, 'é o menor número')
elif b >= a >= c:
    print(b, 'é o maior número')
    print(c, 'é o menor número')
elif b >= c >= a:
    print(b, 'é o maior número')
    print(a, 'é o menor número')
elif c >= a >= b:
    print(c, 'é o maior número')
    print(b, 'é o menor número')
else:
    print(c, 'é o maior número')
    print(a, 'é o menor número')
