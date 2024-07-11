import random

# Solicitação de entrada
print('Vamos jogar Pedra, Papel e Tesoura!!')
print('Já fiz minha escolha, faça a sua:')
print(('=' * 10) + 'JOKENPÔ' + ('=' * 10))
Jogador = input('(1) = Pedra\n'
                '(2) = Papel\n'
                '(3) = Tesoura\n')

# Verificação de resposta
try:
    Jogador = int(Jogador)  # Verificação se a resposta é um número inteiro

    if Jogador < 1 or Jogador > 3:
        print('Apenas números entre 1 a 3 são válidos!')  # Verificação se a resposta está entre 1 e 3

    else:

        if Jogador == 1:
            print(('=' * 3) + 'Você escolheu PEDRA!' + ('=' * 3))
        elif Jogador == 2:
            print(('=' * 3) +'Você escolheu PAPEL!' + ('=' * 3))
        else:
            print(('=' * 3) + 'Você escolheu TESOURA!' + ('=' * 3))


        # Escolha do computador
        Computador = random.randint(1, 3)

        if Computador == 1:
            print(('=' * 3) +'Eu escolhi PEDRA!' + ('=' * 3))
        elif Computador == 2:
            print(('=' * 3) + 'Eu escolhi PAPEL!' + ('=' * 3))
        else:
            print(('=' * 3) + 'Eu escolhi TESOURA!' + ('=' * 3))

            # Lógica e resultado do jogo
        if Computador == Jogador:
            print(('=' * 3) + 'Empatamos!!' + ('=' * 3))
        elif Jogador == 1 and Computador == 3 or Jogador == 2 and Computador == 1 or Jogador == 3 and Computador == 2:
            print(('=' * 3) + 'Parabéns, você ganhou!!' + ('=' * 3))
        else:
            print(('=' * 3) + 'Que pena, você perdeu!!' + ('=' * 3))

except ValueError:
    print('Apenas números entre 1 a 3 são válidos!')
