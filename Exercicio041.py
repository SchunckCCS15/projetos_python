# Recebe a idade como entrada
idade = int(input("Digite a idade: "))

# Verifica e responde o que a pessoa pode fazer com base na idade
if idade <= 9:
    print("MIRIM.")
elif idade <= 14:
    print("INFANTIL.")
elif idade <= 19:
    print("JUNIOR.")
elif idade <= 20:
    print("SÊNIOR")
else:
    print("MASTER")
