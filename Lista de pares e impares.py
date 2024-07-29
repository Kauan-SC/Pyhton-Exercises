quantidade = int(input('Quantos números deseja inserir??  '))
lista = []
pares = []
impares = []
cont = 0
for c in range(quantidade):
    cont += 1
    valor = int(input('Insira um valor:  '))
    lista.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

lista.sort()
print(f'Foram inseridos {cont} valores, que são: {lista}')
print('Entre eles temos:\n')
print(('#' * 10) + 'Pares'.center(20) + ('#' * 10),end='')
print(('#' * 10) + 'Impares'.center(20) + ('#' * 10))
print(f' {pares}'.center(39),end='')
print(f' {impares}'.center(39))
