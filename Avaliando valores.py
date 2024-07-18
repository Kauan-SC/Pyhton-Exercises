# Solicitação de entrada
valor = float(input('Digite um valor:  '))
cont = 0
soma = 0

while valor != 0:  # Lógica da avaliação, que só para quando o usuário escreve o número 0
    cont += 1
    soma += valor
    valor = float(input('Digite outro valor:  \n'
                        'Para finalizar dgite 0\n'))

print('FIM\n'
      f'Você escrevey {cont} números, a soma deles é de {soma}')  # Resultado
