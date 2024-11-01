# Bibliotecas
import time
import random

# Variáveis
historico = {}
faltas = [0,1,2,3,4,5]
prob_faltas = [0.5,0.1,0.1,0.1,0.1,0.05]
hattrick = 0
cart_amarelo = 0
quant_gols = 0
quant_assistencias = 0
quant_faltas = 0
expulsao = 0
quant_amarelos = 0

# Título
print('-='*40)
print('Historico do jogador'.center(80))
print('-='*40,'\n')

# Solicitação de entrada
jogador = str(input('Qual jogador deseja buscar??  ')).capitalize()
partidas = int(input(f'Deseja ver o histórico de quantas partidas??  '))
print('-='*40)

# Historicos de gols,assistências e faltas
for i in range(1, partidas+1):

    if cart_amarelo == 3:  # Caso o jogador leve 3 amarelos, será expulso do próximo jogo
        print('-=' * 40)
        print(f'{jogador} foi expulso do jogo {i}!!!'.center(80))
        print('-=' * 40)
        cart_amarelo = 0
        expulsao += 1

        continue  # Pula para próximo jogo

    historico['gols'] = random.randint(0, 3)  # Marca os gols
    quant_gols += historico['gols']
    historico['assistencias'] = random.randint(0, 5)  # Marcas as assistências
    quant_assistencias += historico['assistencias']
    historico['faltas'] = random.choices(faltas, weights=prob_faltas, k=1)[0]  # Marcas as faltas,com certa probabilidade para quantidade de faltas
    quant_faltas += historico['faltas']

    # Resultado das partidas
    print(f'Durante a partida {i}, o {jogador} fez:'.center(80))
    print(f'{historico["gols"]} gol(s).'.center(80))

    if historico['gols'] == 3:  # Caso o jogador faça 3 gols em uma partida
        print('HAT TRICK!!!'.center(80))
        hattrick += 1
    else:
        pass

    print(f'Deu {historico["assistencias"]} assistência(s).'.center(80))
    print(f'Fez {historico["faltas"]} falta(s).'.center(80))

    if historico['faltas'] >= 3:  # Acima de 3 faltas ele leva um cartão amarelo
        print(f'O jogador {jogador} recebeu cartão amarelo!!!'.center(80))
        cart_amarelo += 1
        quant_amarelos += 1

    print('-='*40)

# Media de gols,assistências,faltas e cartões
media_gols = quant_gols/partidas
media_assistencias = quant_assistencias/partidas
media_faltas = quant_faltas/partidas

# Resultado final
print('\nResultado final:')
print(f'O {jogador} fez {quant_gols} gol(s) em {partidas} jogos, com uma média de {media_gols} por jogo!!')
print(f'O {jogador} fez {hattrick} HAT TRICKS!!')
print(f'O {jogador} deu {quant_assistencias} assistências em {partidas} jogos, com uma média de {media_assistencias} por jogo!!')
print(f'O {jogador} fez {quant_faltas} faltas em {partidas} jogos, com uma média de {media_faltas} por jogo!!')
print(f'O {jogador} recebeu {quant_amarelos} amarelos e foi expulso de {expulsao} jogos!!')
