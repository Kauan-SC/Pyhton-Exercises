import math

# Solicitação de entrada

try:
    Angulo = int(input('Insira qualquer valor de angulo: '))

    # Verificação de valores
    if Angulo <= 0:
        print('Insira um valor positivo!!')
    else:

        # Calculo do Seno,Cosseno e Tangente
        Angulo = math.radians(Angulo)
        Seno = math.sin(Angulo)
        Cosseno = math.cos(Angulo)
        Tangente = math.tan(Angulo)

        # Exibição de resultados
        print('-' * 10)
        print(f'O valor de Seno: {Seno: .1f}\n'
              f'O valor de Cosseno: {Cosseno: .1f}\n'
              f'O valor de Tangente: {Tangente: .1f}\n')
        print('-' * 10)

except ValueError:
    print('Insira valores válidos!!')
