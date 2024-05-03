import math

angulo = float(input('Digite o valor de um ângulo e eu direi o seu seno, cosseno e tangente: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo é {:.2f}, o seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))
