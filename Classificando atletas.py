import datetime

# Solicitação de entrada
print('Vamos classificar qual a sua categoria!!')
Ano_nascimento = input('Insira qual o seu ano de nascimento:  ')
Ano_Atual = datetime.datetime.now().year

# Verificação de resposta
try:
    Ano_nascimento = int(Ano_nascimento)  # Verifica se a resposta inserida é um número e se ele é inteiro
    Idade = Ano_Atual - Ano_nascimento  # Descobrindo a idade
    print(f'Sua idade é {Idade}\n'
          f'Você nasceu no ano de {Ano_nascimento}')

    # Lógica + Resultado
    if Idade > 0 and Idade <= 9:
        print('Sua categoria é a MIRIM.')
    elif Idade > 9 and Idade <= 14:
        print('Sua categoria é a INFANTIL.')
    elif Idade > 14 and Idade <= 19:
        print('Sua categoria é a JUNIOR.')
    elif  Idade > 19 and Idade <= 25:
        print('Sua categoria é a SENIOR.')
    elif Idade > 25 and Idade <= 70:
        print('Sua categoria é a MASTER.')
    elif Idade > 70 and Idade <= 120:
        print('Você tem certeza que ainda consegue ser um atleta??')
    else:
        print('Idade impossível ou inválida!!\n'
              'Por favor insira uma idade adequada.')


except ValueError:
    print('Apenas números inteiros são permitidos!!')