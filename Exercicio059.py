sair = 0
while sair == 0:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    respota = 0
    print('O que deseja fazer com esses números?---------------- ')
    print('[1]Somar')
    print('[2]Multiplicar')
    print('[3]Maior')
    print('[4]Novos Números')
    print('[5]Sair do Programa')
    escolha = int(input('Qual é a sua escolha? '))
    if escolha == 1:
        resposta = n1 + n2
        print('A resposta é {}'.format(resposta))
    elif escolha == 2:
        resposta = n1*n2
        print('A resposta é {}'.format(resposta))
    elif escolha == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        if n2 > n1:
            print('{} é maior que {}')
    elif escolha == 4:
        print('Então digite novamente')
    else:
        sair = 1
print('Fim do programa')
