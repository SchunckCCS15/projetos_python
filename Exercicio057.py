sexo = input('Digite seu sexo [M/F]: ').upper()
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite apenas M ou F: ').upper()
if sexo == 'M':
    print('Parabéns, moço!')
else:
    print('Parabéns, moça!')

