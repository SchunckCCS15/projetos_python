p = int(input('Digite um número: '))
vezes = int(input('Digite quantos primeiro números da sequência: ')) - 2
x = p - 1
contador = 0
resposta = 0
print(' {} '.format(x), end='->')
print(' {} '.format(p), end='->')
while contador < vezes:
    p = x+p
    x = p-x
    print(' {} '.format(p), end='->')
    contador += 1
print('Essa é a sequncia de Fibonacchi')
