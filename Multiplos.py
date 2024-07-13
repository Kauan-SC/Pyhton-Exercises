# Solicitação de entrada
print('Insira um número e eu te mostrarei quantos multiplos até 500 ele tem\n'
      'E a soma desses multiplos.')
Numero = input('Insira seu número:  ')
Multiplo = 0
Soma = 0
Nao_multiplo = 0
Soma_nao_multiplos = 0

try:
    Numero = int(Numero)  # verificação se a resposta é um número inteiro

    if Numero >= 1 or Numero <= 500:  # Verificação se os números estão entre 0 e 500

        for c in range(1, 501):
            if c % Numero == 0:  # Lógica para que apenas os multiplos sejam somados
                Multiplo += 1  # Soma da quantidade de multiplos
                Soma += c  # Soma geral dos multiplos
            else:
                Nao_multiplo += 1  # Soma da quantidade de não multiplos
                Soma_nao_multiplos += c  # Soma geral dos não multiplos
    else:
        print('Apenas valores entre 0 e 500 são possíveis!!')

    print(f'Esse número tem {Multiplo} multiplos\n'
          f'A soma dos multiplos é de {Soma}\n'
          f'Esse número tem {Nao_multiplo} números que não são seus multiplos\n'
          f'A soma dos não multiplos é de {Soma_nao_multiplos}')
except ValueError:
    print('Apenas números inteiros são válidos!!')
