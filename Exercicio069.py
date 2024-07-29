contador_idade = 0
contador_sexoM = 0
contador_sexo_idadeF = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo [F/M]: ')).upper()
    escolha = str(input('Deseja continuar?[S/N]: ')).upper()
    if idade >= 18:
        contador_idade += 1
    if sexo == 'M':
        contador_sexoM += 1
    if sexo == 'F' and idade < 20:
        contador_sexo_idadeF +=1
    if escolha == 'N':
        break
print(f'{contador_idade} pessoas tem mais de 18 anos')
print(f'{contador_sexoM} homens foram cadastrados')
print(f'{contador_sexo_idadeF} mulheres tem menos de 20 anos')
