def conversão(horas, min):
    if horas <= 12:
        h = horas
        m = min
        if horas != 12:
            periodo = 'A.M.'
        else:
            periodo = 'P.M.'
    else:
        lista_horas_24 = list(range(13, 24))
        lista_horas_12 = list(range(1, 12))

        for i in range(len(lista_horas_24)):
            if horas == lista_horas_24[i]:
                h = lista_horas_12[i]
                m = min
                periodo = 'P.M.'
    return h, m, periodo


def horario(h, m, periodo):
    print(f'{h:02}:{m:02} {periodo}')
    return
    
continuar = 1

while continuar == 1:

    horas = int(input('Digite as horas: '))
    min = int(input('Digite os minutos: '))

    h, m, periodo = conversão(horas, min)


    horario(h, m, periodo)

    continuar = int(input('Digite 1 para continuar e 0 para encerrar o programa: '))
