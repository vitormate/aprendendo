#Não consegui entender como fazer esse problema, precisei olhar para solução
#Acho que não compreendi a matemática

x = float(input('Digite um número real: '))
n = int(input('Digite um número inteiro: '))

cos = termo = 1

for i in range(1, n+1):
    termo *= (-(x**2)/(2*i*(2*i-1)))
    cos += termo

print(f'O cosseno de {x} é {cos}')
