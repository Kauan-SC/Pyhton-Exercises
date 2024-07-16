# Solicitação de entrada
print('Digite um número e eu te direi se ele é primo ou não!!')
Numero = input('Seu número é:  ')
Contador = 0
Contador2 = 0

try:
    Numero = int(Numero)  # Verificação se a resposta é um número inteiro

    for c in range(1, Numero + 1):  # Lógica para contar o número de divisores do número escolhido pelo usuário
        if Numero % c == 0:
            print('\33[33m', end='')
            Contador += 1
        else:
            print('\33[31m', end='')
            Contador2 += 1
        print(c,end=' ')

except ValueError:
    print('Apenas números inteiros são válidos!!')

if Contador == 2:
    print('\n\33[mEsse número é primo, tem apenas dois divisores\n'
          f'Que é o número 1 e o número {Numero}')  # Resultado para número primo
else:
    print(f'\n\33[mEsse número não é primo, ele tem {Contador} números que o dividem')  # Resultado para número não primo

