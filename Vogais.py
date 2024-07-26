print('_' * 30)
print('Identificador de Vogais'.center(30))
print('_' * 30)

palavra = str(input('Digite uma palavra(sem assento) e vou identificar as vogais:  '))
vogais = 'aeiouAEIOU'
cont = 0

print(f'As vogais da palavra {palavra} são: ', end='')
for c in palavra:
    if c in vogais:
        cont += 1
        resultado = ''
        resultado += c
        print(resultado, '' , end='')

print(f'\nTemos {cont} vogais!!')