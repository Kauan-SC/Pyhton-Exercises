import math

# Solicitação de entrada
print(('#=#' * 10) + ' Caixa Eletrônico ' + ('#=#' * 10))
valor_sacar = int(input('\nDigite o valor o qual você deseja sacar:  '))

while True:
    n50 = valor_sacar // 50  # Lógica para saber quantas notas de 50 serão enviadas
    if n50 >= 1:
        sobra = n50
        sobra = sobra * 50
        sobra = valor_sacar - sobra  # Diminuindo o valor total pela quantidade de notas possíveis de R$50,00
        valor_sacar = sobra
        if sobra == 0:
            print(f'Você vai receber:\n'
                  f'{n50} notas de R$50,00')  # Lógica caso o n50 seja um número inteiro
            break
        else:
            pass
    else:
        sobra = valor_sacar

    n20 = sobra // 20  # Lógica para saber quantas notas de 20 serão
    if n20 >= 1:
        sobra2 = n20
        sobra2 = sobra2 * 20
        sobra2 = sobra - sobra2
        valor_sacar = sobra2
        if sobra2 == 0:
            print(f'Você vai receber:\n'
                  f'{int(n50)} notas de R$50,00\n'
                  f'{int(n20)} notas de R$20,00')
            break
        else:
            pass
    else:
        sobra2 = valor_sacar

    n10 = sobra2 // 10
    if n10 >= 1:
        sobra3 = n10
        sobra3 = sobra3 * 10
        sobra3 = sobra2 - sobra3
        valor_sacar = sobra3
        if sobra3 == 0:
            print(f'Você vai receber:\n'
                  f'{int(n50)} notas de R$50,00\n'
                  f'{int(n20)} notas de R$20,00\n'
                  f'{int(n10)} notas de R$10,00')
            break
        else:
            pass
    else:
        sobra3 = valor_sacar

    n5 = sobra3 // 5
    if n5 >= 1:
        sobra4 = n5
        sobra4 = sobra4 * 5
        sobra4 = sobra3 - sobra4
        valor_sacar = sobra4
        if sobra4 == 0:
            print(f'Você vai receber:\n'
                  f'{n50} notas de R$50,00\n'
                  f'{n20} notas de R$20,00\n'
                  f'{n10} notas de R$10,00\n'
                  f'{n5} notas de R$5,00')
            break
        else:
            pass
    else:
        sobra4 = valor_sacar

    n2 = sobra4 // 2
    if n2 >= 1:
        sobra5 = n2
        sobra5 = sobra5 * 2
        sobra5 = sobra4 - sobra5
        valor_sacar = sobra5
        if sobra5 == 0:
            print(f'Você vai receber:\n'
                  f'{n50} notas de R$50,00\n'
                  f'{n20} notas de R$20,00\n'
                  f'{n10} notas de R$10,00\n'
                  f'{n5} notas de R$5,00\n'
                  f'{n2} notas de R$2,00')
            break
        else:
            pass
    else:
        sobra5 = valor_sacar

    n1 = sobra5 // 1
    if n1 >= 1:
        sobra6 = n1
        sobra6 = sobra6 * 1
        sobra6 = sobra5 - sobra6
        print(f'Você vai receber:\n'
              f'{n50} notas de R$50,00\n'
              f'{n20} notas de R$20,00\n'
              f'{n10} notas de R$10,00\n'
              f'{n5} notas de R$5,00\n'
              f'{n2} notas de R$2,00\n'
              f'{n1} moedas de R$1,00')
        break
