# Solicitação de entrada
total = 0
cont = 0

while True:
    valor = input('Insira um valor:  ')
    try:
        valor = int(valor)
        total += valor
        cont += 1
    except ValueError:
        break

media = total / cont
print(f'Somas dos valores = {total}\n'
      f'A media dos valores = {media}\n'
      f'Quantidades de números = {cont}')

