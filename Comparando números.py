# Solicitação de entrada
print('Vou comparar dois valores!!')
N1 = input('Insira um valor:  ')

try:
    N1 = float(N1)  # Verificação de resposta
    N2 = input('Insira outro valor:  ')
    N2 = float(N2)  # Verificação de resposta

    # Resultado
    if N1 > N2:
        print(f'O número {N1} é maior que o número {N2}')
    elif N2 > N1:
        print(f'O número {N2} é maior que o número {N1}')
    elif N1 == N2:
        print('Os dois números são iguais!!')
    else:
        print('ERROR!!')

except ValueError:
    print('Apenas números são validos!!')
