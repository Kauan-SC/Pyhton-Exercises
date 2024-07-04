# Solicitação de entrada
Numero = input('Insira um número:  ')

# Verificação do número
try:

    Numero = int(Numero)

    # Segunda solicitação
    Base = input('Agora escolha se quer que esse número seja escrito em:\n'
                 '1 - Binário\n'
                 '2 - Octal\n'
                 '3 - Hexadecimal\n')
    Base = int(Base)

    # Resultado
    if Base == 1:
        print(f'Esse número em binário é: {bin(Numero)[2:]}')
    elif Base == 2:
        print(f'Esse número em octal é: {bin(Numero)[2:]}')
    elif Base == 3:
        print(f'Esse número em hexadecimal é: {hex(Numero)[2:].upper()}')
    else:
        print('Esse não é um número válido!!')

except ValueError:
    print('Apenas números são válidos!!')

