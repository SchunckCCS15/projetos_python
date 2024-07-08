ValorCasa = float(input('Digite o valor da casa que você deseja comprar: '))
Salario = float(input('Digite o seu salário: '))
Anos = int(input('Digite em quantos anos você pagará esse emprestimo: '))

prest = ValorCasa // 12
n1 = (30/100) * prest
if Salario < n1:
    print('Infelizmentenão podemos liberar o emprestimo')
else:
    print('Aproveite sua nova casa!!!')
