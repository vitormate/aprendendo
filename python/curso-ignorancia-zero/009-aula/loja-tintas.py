area = int(input('Tamanho em m² da área a ser pintada: '))

litros = area // 3
if (area % 3) > 0:
    litros += 1

latas = litros // 18
if (litros % 18) > 0:
    latas += 1

valor = latas * 80

print(f'Você vai precisar de {latas} latas.')
print(f'O valor total é R$ {valor:.2f}')
