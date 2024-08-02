from random import randint
cont = 0
while True:
    escolha = int(input('Escolha par[1] ou ímpar[2]: '))
    numero = int(input('Escolha seu número: '))
    numero_robo = randint(0,10)
    resposta = numero + numero_robo
    print(f'Eu escolho o número {numero_robo}')
    if resposta % 2 == 0 and escolha == 1:
        print('Você ganhou parabéns')
        cont += 1
    elif resposta % 2 != 0 and escolha == 2:
        print('Você ganhou parabéns')
        cont += 1
    else:
        print('Você Perdeu')
        break
print(f'Você ganhou {cont} veze(s) !!!')
