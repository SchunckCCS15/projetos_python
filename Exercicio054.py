s = 0
d = 0
p = 1
for c in range(0, 7):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? '.format(p)))
    p += 1
    r = 2024-nascimento
    if r < 18:
        s += 1
    else:
        d += 1
print('A quantidade de menores de idade são de {}'.format(s))
print('A quantidade de maiores de idade são de {}'.format(d))
