# Solicitação de entrada
Nascimento = input('Qual ano você nasceu??  ')

try:
    Nascimento = int(Nascimento)  # Verificação de resposta
    Ano_atual = 2024
    Idade = Ano_atual - Nascimento
    if Idade == 18:
        print('Você tem a idade exata para se alistar!!\n'
              'Aliste-se já.')
    elif Idade > 18 and Idade < 100:
        A = Idade - 18
        C = Nascimento + 18
        print(f'Você passou {A} anos de se alistar')
        print(f'Você deveria ter se alistado no ano de {C}')
    elif Idade > 0 and Idade < 18:
        B = 18 - Idade
        C = Nascimento + 18
        print(f'Faltam {B} anos para você se alistar')
        print(f'Você vai se alistar no ano de {C}')
    else:
        print('Valor inválido!!')
        print('É impossível ter essa idade.')

except ValueError:
    print('Apenas números são válidos!!')