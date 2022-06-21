def somaImposto(custo, taxaImposto):
    custo = custo + custo * (taxaImposto/100)
    return custo

custo_normal = float(input('Digite o custo(R$): '))
taxa = float(input('Digite a taxa de imposto(%): '))

print(f'O custo recalculado com o imposto é de R$ {somaImposto(custo_normal, taxa):.2f}')