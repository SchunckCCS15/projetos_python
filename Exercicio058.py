import random

nRandom = random.randrange(1, 10)
print('SHHHH: {}'.format(nRandom))
n = int(input('Descubra o número que eu pensei entre 1 e 10: '))
tentativas = 0
while n != nRandom:
    n = int(input('Número errado tente novamente: '))
    tentativas += 1
print('Parabéns, você acertou!!!')
print('Você precisou de {} tentavivas para me ganhar'.format(tentativas))

