# Solicitação de entrada
print(('#' * 10) + ' CADASTRO ' + ('#' * 10))
cont_idade = 0
cont_sexo = 0
cont1 = 0

while True:
    nome = str(input('Insira o nome:  '))
    idade = int(input('Insira a idade:  '))
    if idade > 18:
        cont_idade += 1
    sexo = int(input('Insira o sexo:\n'
                     '(1) - Masculino\n'
                     '(2) - Feminino\n'
                     '(3) - Outro\n'))
    if sexo == 1:
        cont_sexo += 1
    elif sexo == 2 and idade < 20:
        cont1 += 1
    programa = int(input('Deseja continuar??\n'
                         '(1) - Sim\n'
                         '(2) - Não\n'))
    if programa == 1:
        pass
    elif programa == 2:
        break
    else:
        while programa != 1 and programa != 2:
            programa = int(input('Deseja continuar??\n'
                                 '(1) - Sim\n'
                                 '(2) - Não\n'))

print(f'{cont_idade} pessoas tem mais de 18\n'
      f'{cont_sexo} pessoas são mulheres\n'
      f'{cont1} pessoas são mulheres com menos de 20 anos')