# Solicitação de entrada
print('Vou somar números para você!!')
Escolha = input('Você quer que eu some:\n'
                '(1) = Pares\n' 
                '(2) = Impares\n')
Total_par = 0
Total_impar = 0
Soma_par = 0
Soma_impar = 0

try:
    Escolha = int(Escolha)  # Verificação de resposta
    for c in range(0, 6):
        Numero = int(input('Escolha seu número:  '))
        if Numero % 2 == 0:  # Lógica para somar números pares
            Total_par += Numero
            Soma_par += 1
        else:
            Total_impar += Numero  # Lógica para somar números impares
            Soma_impar += 1

# Resultado final
    if Escolha == 1:
        print(f'Foram somados {Soma_par} números pares\n'
              f'A soma total deu {Total_par}')
    else:
        print(f'Foram somados {Soma_impar} números impares\n'
              f'A soma total deu {Total_impar}')

except ValueError:
    print('Apenas números inteiros são válidos!!')
