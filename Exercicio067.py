cont = 1
while True:
    num_tabuada = int(input('Quer ver a tabuada de qual valor?: '))
    if num_tabuada < 0:
        break
    print('-'*20)
    for p in range(1, 11):
        print(f'{num_tabuada} x {cont} = {num_tabuada*cont}')
        cont += 1
    cont = 1
    print('-'*20)
print('Programa tabuada encerrado')
