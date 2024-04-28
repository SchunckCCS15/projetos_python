metros = int(input('Quantos metros você quer converter? '))
centimetros = metros * 100
milimetros = metros * 1000
decimetros = metros * 10
hectometros = metros / 100
quilometros = metros / 1000

print('Isso da {:.0f}cm, {:.0f}mm, {:.0f}dm, {:.2f}hm, {:.3f}km'.format(centimetros, milimetros, decimetros, hectometros, quilometros))
