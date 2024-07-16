import datetime

# Solicitação de entrada
print('Vamos analisar idades!!')
Pessoas = input('Insira quantas pessoas são:  ')
Ano_atual = datetime.datetime.now().year
Maioridade = 0
Menor_de_18 = 0


try:
    Pessoas = int(Pessoas)
    for c in range(1, Pessoas + 1):  # Lógica
        Nascimento = int(input(f'Insira o ano de nascimento da pessoa número {c}:  '))
        if Ano_atual - Nascimento >= 18:  # Verificação se a pessoa possui maioridade
            Maioridade += 1
        elif 0 < Ano_atual - Nascimento < 18:
            Menor_de_18 += 1
        else:
            print('Idade impossível!!')

    print(f'Existem {Maioridade} pessoas acima de 18 anos!!\n'
          f'Existem {Menor_de_18} pessoas menores de idade!!')

except ValueError:
    print('Apenas números inteiros são válidos!!')
