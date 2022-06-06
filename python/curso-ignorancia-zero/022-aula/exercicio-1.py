salario = float(input('Salário do funcionário: '))


aumento = percentual = novo_salario = 0
if salario <= 280:
    percentual = 20
    aumento = salario * 0.2
    novo_salario = salario + aumento

elif salario > 280 and salario <= 700:
    percentual = 15
    aumento = salario * 0.15
    novo_salario = salario + aumento

elif salario > 700 and salario <= 1500:
    percentual = 10
    aumento = salario * 0.1
    novo_salario = salario + aumento

else:
    percentual = 5
    aumento = salario * 0.05
    novo_salario = salario + aumento

print(f'\nSalário antigo: R$ {salario:.2f}')
print(f'Percentual de aumento aplicado: {percentual}%')
print(f'Valor de aumento: R$ {aumento:.2f}')
print(f'Novo salário: R$ {novo_salario:.2f}')
