primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
resultado = primeiro
contador = 0

# Primeiros 10 termos
while contador < 10:
    print(' {} '.format(resultado), end=' -> ')
    resultado += razao
    contador += 1
print('...')

# Perguntar se o usuário quer mais termos
while True:
    nao = input('Deseja mais termos?[S/N] ').upper()
    if nao == 'N':
        print('Fim do programa')
        break
    elif nao == 'S':
        qntd = int(input('Quantos termos você deseja? '))
        cont = 0
        while cont < qntd:
            print(' {} '.format(resultado), end=' -> ')
            resultado += razao
            cont += 1
        print('...')
    else:
        print('Entrada inválida. Por favor, responda com S ou N.')
