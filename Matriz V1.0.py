# Solicitação de entrada
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
soma = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor: '))

# Lógica
# Contagem de números pares
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            par += 1

# Soma da coluna 3
for l in range(0, 3):
    soma += matriz[l][2]

# Maior valor linha 2
maior = max(matriz[1])

# Resultado
for l in range(0, 3):
    for c in range(0, 3):
        print(f'({matriz[l][c]:^5})', end=' ')
    print()

print(f'\nTivemos {par} números pares!!')
print(f'A soma dos valores da coluna 3 é {soma}!!')
print(f'O maior valor da linha 2 é {maior}!!')


