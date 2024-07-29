num = int(input("Digite um número para calcular o fatorial: "))
resultado = 1
contador = num

while contador != 0:
    resultado *= contador
    contador -= 1

print('{}! = {}'.format(num, resultado))

'''num = int(input("Digite um número para calcular o fatorial: "))
resultado = 1

for i in range(1, num + 1):
    resultado *= i

print(f"O fatorial de {num} é {resultado}")'''

