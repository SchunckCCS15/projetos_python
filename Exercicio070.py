total_de_gastos = produto_mais_de_mil = 0
produto_mais_barato_nome = ''
produto_mais_barato_preco = None

while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    escolha = str(input('Deseja continuar?[S/N]: ')).upper()

    total_de_gastos += preco

    if preco > 1000:
        produto_mais_de_mil += 1

    if produto_mais_barato_preco is None or preco < produto_mais_barato_preco:
        produto_mais_barato_preco = preco
        produto_mais_barato_nome = nome

    if escolha == 'N':
        break

print(f'O total de gasto da sua compra ficou em {total_de_gastos}R$')
print(f'{produto_mais_de_mil} produtos custam mais de mil reais')
print(f'{produto_mais_barato_nome} é o produto mais barato')
