cont = 0
valores = []
while True:
    cont += 1
    valor = int(input('Insira um valor:  '))
    valores.append(valor)
    r1 = str(input('Deseja continuar?? (S/N)  ')).upper()
    while r1 != 'S' and r1 != 'N':
        r1 = str(input('Deseja continuar?? (S/N)  ')).upper()
    if r1 == 'S':
        pass
    else:
        break

valores.sort(reverse=True)
print(f'Foram inseridos {cont} valores!!')
print(f'A lista de forma decrescente é: {valores}')
if 5 in valores:
    print(f'O valor 5 está na lista, na posição {valores.index(5) + 1}')
else:
    pass