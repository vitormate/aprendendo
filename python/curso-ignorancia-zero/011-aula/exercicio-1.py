num = int(input('Digite um número entre 0 e 999: '))
resto = num

centenas = num // 100
resto = resto % 100

dezenas = resto // 10
resto = resto % 10

unidades = resto // 1

if num >= 1000:
    print('Entrada Inválida!')
elif num < 0:
    print('Entrada Inválida!')
else:
    if centenas > 1:
        if dezenas > 1:
            if unidades > 1:
                print(f'{num} = {centenas} centenas, {dezenas} dezenas e {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {centenas} centenas, {dezenas} dezenas e {unidades} unidade')
            else:
                print(f'{num} = {centenas} centenas e {dezenas} dezenas')
        elif dezenas == 1:
            if unidades > 1:
                print(f'{num} = {centenas} centenas, {dezenas} dezena e {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {centenas} centenas, {dezenas} dezena e {unidades} unidade')
            else:
                print(f'{num} = {centenas} centenas e {dezenas} dezena')
        else:
            if unidades > 1:
                print(f'{num} = {centenas} centenas e {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {centenas} centenas e {unidades} unidade')
            else:
                print(f'{num} = {centenas} centenas')

    elif centenas == 1:
        if dezenas > 1:
            if unidades > 1:
                print(f'{num} = {centenas} centena, {dezenas} dezenas e {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {centenas} centena, {dezenas} dezenas e {unidades} unidade')
            else:
                print(f'{num} = {centenas} centena e {dezenas} dezenas')
        elif dezenas == 1:
            if unidades > 1:
                print(f'{num} = {centenas} centena, {dezenas} dezena e {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {centenas} centena, {dezenas} dezena e {unidades} unidade')
            else:
                print(f'{num} = {centenas} centena e {dezenas} dezena')
        else:
            if unidades > 1:
                print(f'{num} = {centenas} centena e {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {centenas} centena e {unidades} unidade')
            else:
                print(f'{num} = {centenas} centena')

    else:
        if dezenas > 1:
            if unidades > 1:
                print(f'{num} = {dezenas} dezenas e {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {dezenas} dezenas e {unidades} unidade')
            else:
                print(f'{num} = {dezenas} dezenas')
        elif dezenas == 1:
            if unidades > 1:
                print(f'{num} = {dezenas} dezena e {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {dezenas} dezena e {unidades} unidade')
            else:
                print(f'{num} = {dezenas} dezena')
        else:
            if unidades > 1:
                print(f'{num} = {unidades} unidades')
            elif unidades == 1:
                print(f'{num} = {unidades} unidade')
            else:
                print(f'{num} = Zero')
