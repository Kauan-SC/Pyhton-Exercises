import time

# Solicitação de entrada
print('Vou te mostrar a sequencia de Fibonacci!!')
termos = int(input('Insira quantos termos deseja:  '))
f2 = 0
f1 = 1
cont = 0

while cont < termos:
    time.sleep(0.5)
    print(f2, '-> ', end='')
    ftotal = f1 + f2
    f2 = f1
    f1 = ftotal
    cont += 1