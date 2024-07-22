# Solicitação de entrada
print(('-_' * 10) + ' TABUADA '+ ('-_' * 10))
c = int

while True:
    valor = input('Insira um valor:  ')
    try:
        valor = int(valor)
        for c in range(1, 10 + 1):
            resultado = valor * c
            print(f'{valor} X {c} = {resultado}')

    except ValueError:
        break