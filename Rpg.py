import random

def personagem():
    força = random.randint(1, 10)
    print('Você tem {} pontos de força'.format(força))


def batalha():
    print('Você encontrou um monstro, o que deseja fazer?')
    vidaMonstro = 100
    while vidaMonstro > 0:
        print('O monstro tem {} de vida'.format(vidaMonstro))
        opção = int(input('1-Bater, 2-Chutar, 3-Informações dos golpes: '))

        if opção == 1:
            print('Você bateu no monstro e tirou 20 de dano')
            vidaMonstro = vidaMonstro - 20
        if opção == 2:
            print('Você chutou o monstro e tirou 40 de dano')
            vidaMonstro = vidaMonstro - 40
        if opção == 3:
            print('Bater tira 20 de dano e chutar tira 40 de dano')
    print('Parabéns você ganhou a luta e o mosntro fugiu!!!!!!')


personagem()
batalha()
