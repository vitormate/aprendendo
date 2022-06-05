n = float(input('Digite um número: '))

if n == int(n):
    print(f'{n} é inteiro.')
else:
    print(f'{n} é decimal.')
    decimal = n - int(n)
    arredondado = int(n)

    if decimal >= 0.5:
        arredondado += 1
        
    print(f'{n} arredondado: {arredondado}')

#round(x) -> Faz exatamente o que esse código faz
# arredonda número da forma correta sem a necessidade
# de mais códigos.