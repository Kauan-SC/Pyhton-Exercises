import random

numero = []
total = 0
for c in range(0, 5):
    valor = random.randint(0, 100)
    numero.append(valor)
    total += valor

print(f'Os números sorteados foram: {numero}')
maior = max(numero)
menor = min(numero)
quantidade = len(numero)
media = total / quantidade

print(f'O maior valor é: {maior}\n'
      f'O menor valor é: {menor}\n'
      f'A soma desses valores é: {total}\n'
      f'A media da soma é: {media}')
