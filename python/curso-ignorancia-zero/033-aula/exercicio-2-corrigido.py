def converter(hora):
    return hora - 12

def imprimirHorario(hora, min):
    if hora <= 12:
        print(f'{hora:02}:{min:02} A.M.')
    else:
        print(f'{converter(hora):02}:{min:02} P.M.')



continuar = 1

while continuar == 1:

    hora = int(input('Digite a hora: '))
    min = int(input('Digite os minutos: '))

    imprimirHorario(hora, min)

    continuar = int(input('Digite 1 para continuar e 0 para encerrar o programa: '))
