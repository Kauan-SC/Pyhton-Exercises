import time

# Solicitação de entrada
print(('=-=' * 5) + ' FATORIAL ' + ('=-=' * 5))
valor = int(input('Insira um número inteiro:  '))
n1 = 1

print(f'Calculando fatorial de {valor}! ', end='')
while valor > 0:  # Lógica do fatorial
    time.sleep(0.5)  # Pausa de 1 segundo
    print(f'{valor} ', end='')
    print('X ' if valor > 1 else '= ',end='')
    n1 *= valor
    valor -= 1
print(n1, end='')



