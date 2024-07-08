idade = int(input('Digite sua idade: '))
if idade < 18:
    falta = 18 - idade
    print('Você ainda vai se alistar. Falta(m) {} ano(s) para você se alistar.'.format(falta))
elif idade > 18:
    precisa = idade - 18
    print('Você já deveria ter se alistado. Passaram-se {} anos da época certa'.format(precisa))
else:
    print('Está na hora de se alistar!')
