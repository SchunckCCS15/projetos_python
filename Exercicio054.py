s = 0
d = 0
for c in range(0, 7):
    nascimento = int(input('Digite o ano de seu nascimento: '))
    r = 2024-nascimento
    if r < 18:
        s += 1
    else:
        d += 1
print('A quantidade de menores de idade são de {}'.format(s))
print('A quantidade de maiores de idade são de {}'.format(d))
