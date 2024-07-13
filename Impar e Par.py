print('Vou te falar todos os números Ímpares ou Pares até 100!!')

Escolha = input(('#' * 5) + ' Faça sua escolha ' + ('#' * 5) + "\n"
                "(1) = Números Ímpares\n"
                "(2) = Números Pares\n")

try:
    Escolha = int(Escolha)  # Utilização do try para verificar se a resposta é um número
    if Escolha == 1:
        print('Você escolheu os números impares')
        for c in range(1, 100, 2):
            print(f'Número {c}     ')
    elif Escolha == 2:
        print('Você escolheu os números pares')
        for c in range(2, 101, 2):
            print(f'Número {c}     ')
    else:
        print('Apenas o número 1 ou 2 são válidos!!')

except ValueError:
    print('Apenas o número 1 ou 2 são válidos!!')