preço = float(input('Digite o preço do produto para o desconto ser aplicado: '))
desconto = preço * (5/100)
preço_com_desconto = preço - desconto
print('Este produto custará {:.2f} com 5% de desconto'.format(preço_com_desconto))
