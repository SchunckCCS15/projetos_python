nota1 = float(input('Me fale sua primeira nota: '))
nota2 = float(input('Me fale sua segunda nota: '))

media = (nota1 + nota2) / 2
print('Sua média é: {:.2f}'.format(media))

if media < 5:
    print('Você foi reprovado')
elif media >= 7:
    print('Você foi aprovado')
else:
    print('Você precisa fazer a recuperação')

