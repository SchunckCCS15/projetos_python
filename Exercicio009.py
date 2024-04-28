first = int(input('Me de um número e falarei sua tabuada até o 10: '))
cont = 1
tabuada = 0
while cont <= 10:
    tabuada = first * cont
    print('{} x {} = {}'.format(first, cont, tabuada))
    cont = cont +1
