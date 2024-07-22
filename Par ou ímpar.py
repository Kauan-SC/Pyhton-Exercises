import random

# Solicitação de entrada
print(('#-' * 10) +' Par ou Impar ' + ('#' * 10))
escolha = str(input('Faça sua escolha, Par ou Impar:  ')).upper()
vitorias = 0
jogos = 0

while escolha in ('PAR', 'IMPAR'):
    jogos += 1
    valor = int(input('Escolha um número:  '))
    computador = random.randint(1, 100)
    print(f'Eu escolho {computador}')
    resultado = valor + computador
    if escolha == 'PAR' and resultado % 2 == 0:
        print('Parabéns, você venceu!!\n'
              f'Escolheu {escolha}, o resultado foi {resultado}!!')
        vitorias += 1
    elif escolha == 'IMPAR' and resultado % 2 != 0:
        print('Parabéns, você venceu!!\n'
              f'Escolheu {escolha}, o resultado foi {resultado}!!')
        vitorias += 1
    else:
        print(f'Escolheu {escolha}, o resultado foi {resultado}!!')
        break

print(f'Foram jogadas {jogos} partidas\n'
      f'Você venceu {vitorias} partidas!!')

