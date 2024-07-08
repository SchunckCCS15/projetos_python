import random
import time
print("Bem-vindo aventureiro, sua missão nessa terra é ganhar do monstro chefe. Para isso você deve explorar o mundo, pegar armas e achar o chefe monstro")
time.sleep(3)
print("?: Olá, meu nome é {}".format("Rick"))
time.sleep(3)
print("Rick: Estou aqui apenas para te dar o kit de aventureiro, tome")
time.sleep(3)
print("Você ganhou: Espada, Tocha, Arco e flechas!!!")
time.sleep(3)
print("Rick: Treine com esse monstro descontrolado.")
time.sleep(3)
print("Você encontrou um monstro, o que deseja fazer?")
time.sleep(3)
Vida = 400

def batalha_boss():
    dano_boss=random.randrange(5, 10)
    Vida = Vida-dano_boss
def fugir():
    sorte = random.randrange(0, 10)
    if sorte >= 6:
        print("Você consegiu fugir")
        monstro = 0
    else:
        print("Você não consegue fugir")

def batalha_tutorial():
    monstro = 100
    resposta_batalha = False
    while monstro > 0:
        decisao = int(input("1-Atacar, 2-Fugir: "))
        if decisao == 1:

                ataque = int(input("Como deseja atacar?: 1-Espada, 2-Arco e Flecha: "))

                if ataque == 1:
                    dano = random.randrange(10, 30)
                    print("Você tirou {} de vida do monstro".format(dano))
                    monstro = monstro-dano
                elif ataque == 2:
                    dano_b = random.randrange(10, 45)
                    print("Você tirou {} de vida do monstro".format(dano_b))
                    monstro = monstro-dano_b
                else:
                    print("Responda corretamente")
        elif decisao == 2:
            print("Você não pode fugir dessa batalha amigo!")


batalha_tutorial()
nome = input("Rick: Parabéns é..., desculpe mas qual é seu nome?: ")
print("A sim, parabéns {}, aqui está sua recompensa.".format(nome))
print("---------------------------------------------------------------------------------------")
print("Você recebeu um X_ataque e uma poção")
print("{} colocou os itens na mochila!".format(nome))
print("---------------------------------------------------------------------------------------")
