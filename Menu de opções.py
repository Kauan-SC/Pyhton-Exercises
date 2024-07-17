# Solicitação de entrada
print(('#' * 5) + ' Menu de Opções ' + ('#' * 5))
N1 = float(input('Insira um número:  '))
N2 = float(input('Insira outro número:  '))
c = 0

while c != 7:  # Lógica do menu de opções, caso usuário escolha 7, fecha o programa
    print(('#' * 5) + ' OPÇÕES ' + ('#' * 5))
    c = int(input("(1) - Somar\n"
                  "(2) - Subtrair\n"
                  "(3) - Multiplicar\n"
                  "(4) - Dividir\n"
                  "(5) - Maior e menor\n"
                  "(6) - Novos números\n"
                  "(7) - Finalizar\n"))

    if c == 1:
        NTotal = N1 + N2
        print(f'A soma é igual a: {NTotal}')
    elif c == 2:
        NTotal = N1 - N2
        print(f'A subtração é igual a: {NTotal}')
    elif c == 3:
        NTotal = N1 * N2
        print(f'A multiplicação é igual a: {NTotal}')
    elif c == 4:
        if N2 != 0:
            NTotal = N1 / N2
            print(f'A divisão é igual a: {NTotal}')
        else:
            print('Divisão por zero não é possível!!')
    elif c == 5:
        maior = max(N1, N2)
        menor = min(N1, N2)
        print(f"O maior é {maior}, o menor é {menor}!!")
    elif c == 6:
        N1 = float(input('Insira um número:  '))
        N2 = float(input('Insira outro número:  '))
    elif c == 7:
        pass
    else:
        print('Número inválido!!')

print('FIM')
