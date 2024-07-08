km = int(input('Qual era a velocidade em que o carrou passou em Km? '))
if km >= 80:
    print('Você excedeu o limite de velocidade e foi multado!!!')
    multa = (km - 80) * 7
    print("Sua multa deu: {}R$".format(multa))
else:
    print('Ok, boa viagem!!')

