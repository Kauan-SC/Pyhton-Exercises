print('_' * 30)
print('Avaliador de expressão'.center(30))
print('-' * 30)

while True:
    exp = str(input('Insira uma expressão matemática:  '))
    cont = exp.count('(')
    cont2 = exp.count(')')
    if cont - cont2 == 0:
        print('Expressão correta')
    else:
        print('Expressão incorreta')

