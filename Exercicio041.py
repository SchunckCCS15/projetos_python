# Recebe a idade como entrada
idade = int(input("Digite a idade: "))

# Verifica e responde o que a pessoa pode fazer com base na idade
if idade <= 9:
    print("Você pode fazer a atividade A.")
elif idade <= 14:
    print("Você pode fazer a atividade B.")
elif idade <= 18:
    print("Você pode fazer a atividade C.")
else:
    print("Você pode fazer a atividade D.")
