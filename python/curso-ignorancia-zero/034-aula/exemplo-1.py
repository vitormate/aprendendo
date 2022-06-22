def opMat(num1, num2):
    soma = num1 + num2
    mult = num1 * num2
    div = num1 / num2
    subt = num1 - num2
    #Esse return retorna uma tupla
    return soma, mult, div, subt

#tupla
a = opMat(2,3)

print(a)

#Para imprimir sem o formato de tupla - (x,y,z) - é necessário atribuir uma variável a cada elemento da tupla
# nesse caso são 4 elementos
#Caso use menos ou mais variáveis que elementos ocorrerá um erro. Ex.: a,b = opMat(2, 3) -> erro.

a, b, c, d = opMat(2, 3)

print(a, b, c, d)

