preço = float(input('Digite o preço do produto para o desconto ser aplicado: '))
desconto = preço - (preço * 5/100)
print('Este produto custará {:.2f} com 5% de desconto'.format(desconto))
