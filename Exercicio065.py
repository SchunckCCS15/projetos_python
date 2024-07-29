a = 'S'
maior = menor  = soma = reserva = n = 0
cont = 1
while a == 'S':
    soma += n
    reserva = soma - n
    n = int(input('Digite um valor: '))
    a = str(input('Quer continuar?[S/N]: ')).upper()
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    cont += 1
soma = soma / cont
print('Você digtou {} números e a média foi {:.2f}'.format(cont, soma))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('Acabou')
