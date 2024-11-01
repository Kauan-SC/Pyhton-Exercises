# Importando bibliotecas
import random
import time

# Variáveis
c = 0
dic = {}
resultado = {}

# Solicitação de entrada
print('#' * 25)
print('Jogo de dados em Python'.center(20))
print('#' * 25)

for i in range(1, 5):
    c = random.randint(1, 6)  # Gera um valor entre 1 e 6 do dado
    time.sleep(1)
    print(f'O jogador{i} sorteou: {c}')  # Sorteia um número
    resultado[f'jogador{i}'] = c  # Salva o número do jogador e o valor sorteado

# Resultado
resultado_ordenado = dict(sorted(resultado.items(), key=lambda item: item[1], reverse=True))  # Deixando o maior valor do dado em primeiro
print()
print('#' * 25)
for k, v in resultado_ordenado.items():
    print(f'O jogador {k}: tirou {v}')