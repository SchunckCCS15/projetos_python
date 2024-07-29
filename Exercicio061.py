primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
resultado = primeiro
contador = 0
while contador < 10:
    if contador < 1:
        print(' {} '.format(primeiro), end='->')
        contador += 1
    resultado += razão
    contador += 1
    print(' {} '.format(resultado), end='->')
print('Fim')
