num = int(input('Digite o número de temperaturas registradas: '))

soma = menor = maior = float(input('Digite a temperatura 1: '))


for i in range(2, num+1):
    temperatura = float(input(f'Digite a temperatura {i}: '))

    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
    
    soma += temperatura

print(f'A menor temperatura foi: {menor:6.2f} °C')
print(f'A maior temperatura foi: {maior:6.2f} °C')
print(f'A média das temperaturas é {soma/num:6.2f} °C')
