sal = float(input('Digite seu salário: '))
if sal >= 1.200:
    salM = sal + (sal/10)
    print('Seu salário com o aumento ficou: {}'.format(salM))
else:
    salM2 = sal + (sal/15)
    print('Seu salário com o aumento ficou: {}'.format(salM2))
