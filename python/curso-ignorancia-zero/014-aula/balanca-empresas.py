n = int(input('Digite o número de empresas: '))
m = int(input('Digite o número de meses: '))

empresa = 1
print('')
while empresa <= n:
    print('Empresa', empresa, ':')
    mes = 1
    balanca = 0
    while mes <= m:
        print('Mês', mes, ':')
        ganho = int(input('Digite o ganho da empresa no mes: '))
        gasto = int(input('Digite o gasto da empresa no mês: '))
        balanca = balanca + (ganho - gasto)
        print('')

        mes = mes + 1
    
    if balanca == 0:
        print('A empresa', empresa, 'ficou indiferente(balança = R$ ', balanca, ')')
    elif balanca > 0:
        print('A empresa', empresa, 'fechou com lucro de R$ ', balanca)
    else:
        print('A empresa', empresa, 'fechou com défict de R$ ', balanca)

    empresa = empresa + 1
    print('')
