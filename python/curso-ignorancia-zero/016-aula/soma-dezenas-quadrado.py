n = 1000

while n < 10000:

    primeiraParte = n // 100
    segundaParte = n % 100
    raiz = n**(1/2)

    if raiz == (primeiraParte + segundaParte):
        print(n)
    
    n += 1
