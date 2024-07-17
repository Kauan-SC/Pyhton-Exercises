# Solicitação de entrada
print('Vou analisar seus dados pessoais!!')
Pessoas = input('Insira quantas pessoas serão:  ')
Homem_velho = 0
Nome_homem = ''
Contador = 0
Media = 0

try:  # Verificação se a quantidade de pessoas é um número inteiro
    Pessoas = int(Pessoas)
    for c in range(1, Pessoas + 1):  # Desenvolvimento do programa
        Nome = str(input(f'Insira o nome da pessoa {c}:  '))
        Idade = int(input(f'Agora insira a idade de {Nome}:  '))
        Media += Idade
        Sexo = int(input('O sexo é:\n'
                         '(1) - Masculino\n'
                         '(2) - Feminino\n'
                         '(3) - Outro\n'))
        if Sexo == 1:  # Lógica para gravar a idade e o nome do homem mais velho
            if Idade > Homem_velho:
                Nome_homem = Nome
                Homem_velho = Idade
            else:
                pass
        elif Sexo == 2:  # Lógica para saber quantas mulheres tem menos de 20 anos
            if Idade < 20:
                Contador += 1
            else:
                pass
        elif Sexo == 3:
            pass
        else:
            print('Sexo inválido, por favor escolha uma das opções informadas!!')

except ValueError:
    print('Apenas números inteiros são válidos!!')
    Pessoas = 0  # Evitar erros na hora da divisão

if Pessoas > 0:
    Media1 = Media / Pessoas
    print(f'{Pessoas} pessoas foram analisadas, a média de idade entre elas é de {Media1}\n'
          f'O nome do homem mais velho é {Nome_homem}, com a idade de {Homem_velho} anos!!\n'
          f'O número de mulheres com menos de 20 anos é {Contador} mulheres')
