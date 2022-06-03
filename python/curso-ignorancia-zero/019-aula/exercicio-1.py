n = int(input('Digite um valor para n: '))
i = int(input('Digite um valor para i: '))
j = int(input('Digite um valor para j: '))

c = nat = 0
while c < n:
    if nat % i == 0 or nat % j == 0:
        print(nat)
        c += 1
    nat += 1
