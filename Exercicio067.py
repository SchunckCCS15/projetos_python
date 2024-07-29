cont = 1
while True:
    num_tabuada = int(input('Quer ver a tabuada de qual valor?: '))
    if num_tabuada < 0:
        break
    print('-'*20)
    for p in range(1, 11):
        resultado = num_tabuada * cont
        print(f'{num_tabuada} x {cont} = {resultado}')
        cont += 1
    cont = 1
    print('-'*20)
print('Programa tabuada encerrado')
