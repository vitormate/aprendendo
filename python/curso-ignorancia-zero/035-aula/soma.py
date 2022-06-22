def soma(num1, *lista):
# Ao usar o * dizemos que não sabemas a quantidade 
# de argumentos que será fornecida, fazendo com que todos os 
# argumentos recebidos sejam organizados em uma tupla.
    print(lista)

    soma_num = 0

    for num in lista:
        soma_num += num
    
    return soma_num

a = [1,2,3,4]

print(soma(1,2,3,4,5))