# Bibliotecas
import random
import time

# Variáveis
gols = [0,1,2,3,4]
prob_gols = [0.1,0.1,0.05,0.01,0.00001]
jog_dados = {}

# Titulo
print('=_'*20)
print('Historico do Time!!'.center(40))
print('=_'*20)

# Solicitação de entrada
partidas = int(input('\nQuantas partidas deseja ver?? '))
jogadores = int(input('O historico de quantos jogadores deseja ver??  '))

# Inicialização dos jogadores
for i in range(1, jogadores+1):
    nome = str(input('Digite o nome do jogador: ').capitalize())
    jog_dados[nome] = {'gols': [], 'media': 0, 'total': 0}

# Randomizando número de gols
for nome,dados in jog_dados.items():
    total = 0
    for j in range(1, partidas+1):
        time.sleep(1)
        gol = random.choices(gols, weights=prob_gols, k=1)[0]
        jog_dados[nome]['gols'].append(gol)
        print()
        print('=-'*20)
        print(f'Historico da partida {j} do {nome}!!'.center(40))
        print('=-'*20)
        print(f'{nome} fez {gol} gol(s).')
        total += gol

    jog_dados[nome]['total'] += total
    jog_dados[nome]['media'] = total / partidas if partidas > 0 else 0
    media = 0

# Resultado
print()
for nome,dados in jog_dados.items():
    print(f'O jogador {nome} fez {dados["total"]} gol(s) no total')
    print(f'O jogador {nome} teve uma média de {dados["media"]} gol(s)')

