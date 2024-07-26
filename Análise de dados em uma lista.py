a = int(input('Quantos valores deseja digitar?  '))

valores = []
pares = []
impares = []

for c in range(a):
    valor = int(input('Digite um valor:  '))
    valores.append(valor)

try:
    print(f'O valor 3 está na posição {valores.index(3) + 1}')
except ValueError:
    pass

quantidade = valores.count(9)
print(f'O valor 9 apareceu {quantidade} vezes')

for c in valores:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'Os números pares são {len(pares)}:\n'
      f'{pares}')
print(f'Os números impares são {len(impares)}:\n'
      f'{impares}')
