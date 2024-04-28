altura = float(input('Me fale a atura da parede em metros: '))
largura = float(input('Me fale a largura da parede em metros: '))
area = altura * largura
tintas = area / 2
print('Você precisará de {:.0f} latas de tinta para pintar sua parede'.format(tintas))
