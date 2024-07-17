print('-=' * 20)
valor = float(input('Digite o valor a ser pago em R$: '))
print('Forma de pagamento: 1-Dinheiro, 2-Cheque, 3-Cartão')
forma_pagamento = int(input('Digite sua forma de pagamento:'))
print('-=' * 20)

if forma_pagamento == 1 or forma_pagamento == 2:
    preço = valor - (valor * 10) / 100
    print('-=' * 20)
    print('O seu produto ficou em {:.2f}R$'.format(preço))
else:
     parcela = int(input('Deseja parcelar? 1-Sim, 2-Não: '))
     if parcela == 2:
         preço = valor - (valor * 5)/100
         print('-=' * 20)
         print('O seu produto ficou em {:.2f}R$'.format(preço))
     else:
         parcelar = int(input('Deseja parcelar em quantas vezes?(Máximo até 3 vezes): '))
         if parcelar == 2:
            preço = valor
            print('-=' * 20)
            print('O seu produto ficou em {:.2f}R$'.format(preço))
         else:
             preço = valor + (valor * 20)/100
             print('-=' * 20)
             print('O seu produto ficou em {:.2f}R$'.format(preço))
