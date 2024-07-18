import time

# Solicitação de entrada
print('#' * 23)
print('     Gerador de PA')
print('#' * 23)

repeticao = int(input('\nInsira quantos termos você quer:  '))  # Definição de quantos termos aparecerão
termo1 = int(input('Insira o primeiro termo:  '))
termo2 = int(input('Insira o segundo termo:  '))
c = 0
total = termo1 + termo2
print(termo1,'-> ', end='')

while c != repeticao:  # Lógica da progressão aritmética
    time.sleep(0.5)  # Timer para cada resposta aparecer
    print(total, end='')
    print(' -> ' if c < repeticao -1 else '', end='')  # Resultado
    total = total + termo2
    c += 1


