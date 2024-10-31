# Solicitação de entrada
import random
import time
print('#' * 20)
print('Jogo da Mega Sena'.center(20))
print('#' * 20)

jogos = int(input('Quantos jogos você deseja fazer??\n'))

# Lógica do sorteio
print()
print(('=' * 6) + f'Foram feitos {jogos} jogos' + ('=' * 6))
for i in range(jogos):
    numeros = random.sample(range(1, 60), 6)
    time.sleep(1)
    print(f'Jogo N{i+1}: = ',numeros)


