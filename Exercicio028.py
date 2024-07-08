import random

nRandom = random.randrange(1, 5)
print('SHHHH: {}'.format(nRandom))
n = int(input('Descubra o número que eu pensei entre 1 e 5: '))
if n == nRandom:
    print('Parabéns, você acertou!!!')
else:
    print('Você errou, que pena!!')
