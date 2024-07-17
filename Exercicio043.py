print('-=' * 20)
peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua atura em Metros: "))
print('-=' * 20)

imc = peso / altura**2

print("Seu Imc ficou em {:.2f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.5 and imc <=25:
    print("Você está no peso ideal")
elif imc > 25 and imc <= 30:
    print("Vcê está com sobrepeso")
elif imc > 30 and imc <= 40:
    print("Você está com obesidade")
else:
    print("Você está com obesidade mórbida")
