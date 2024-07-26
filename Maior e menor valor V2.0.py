import random

quantidade = int(input('Quantos números você quer gerar??  '))
v1 = int(input('Valor inicial:  '))
v2 = int(input('Valor final:  '))
lista = []
soma = 0
cont = 0

for c in range(quantidade):
    vfinal = random.randint(v1, v2)
    lista.append(vfinal)
    soma += vfinal
    cont += 1

maior = max(lista)
menor = min(lista)
media = soma / cont
print(f'Os valores são: {lista}', end='')
print(f'\nO maior valor é {maior},que aparece nas posições: ', end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')

print(f'\nO menor valor é {menor}, que aparece nas posições ', end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...')

print(f'\nA soma de todos os valores é: {soma}\n'
      f'A média é: {media:.2f}')
