#nome = input('Qual é seu nome? ')
#print('Prazer em te conhecer {:^20}!'.format(nome))

#n1 = int(input('Um valor: '))
#n2 = int(input('Outro valor: '))
#print('A soma vale{:2}'.format(n1+n2))

n1 = int(input('um valor: '))
n2 = int(input('Outro valor: '))
s = n1+ n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n2 ** n2
print('A soma é {}, \n o produto é {} e a divisão é {:.3f} '.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
