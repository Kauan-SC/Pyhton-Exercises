lista = []
pares = []
impares = []
c = 0

q1 = int(input('Quantos números deseja digitar??  '))

for c in range(q1):
    lista.append(int(input('Insira um valor:  ')))

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'A lista é: {lista}')
print(f'Valores pares: {pares}\n'
      f'Valores impares: {impares}')