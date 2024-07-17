import random

# Solicitação de entrada
print('Vamos jogar um jogo.Vou escolher um número entre 0 e 10\n'
      'Tente adivinhar!!')
Contador = 0

Numero = random.randint(1,10)  # Randomizando escolha do computador
Numero_jogador = int(input('Chute um número:  '))

if 0 <= Numero_jogador <= 10:
    while Numero_jogador != Numero:  # Lógica para caso jogador errar
        print('Você errou!!')
        if Numero_jogador > Numero:  # Lógica para saber se o número está para cima ou para baixo
            print('Menos...')
        else:
            print('Mais...')

        Numero_jogador = int(input('Chute outro número:  '))
        Contador += 1

    print('Você acertou!!')
    print(f'Foram necessárias {Contador} tentativas!!')
else:
    print('Apenas valores entre 0 e 10 são válidos!!')

