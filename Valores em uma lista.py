quantidade = int(input('Quantos valores deseja digitar??  '))
lista = set()
cont = 0

while cont < quantidade:
    lista.add(int(input('Digite um valor:  ')))
    cont += 1
    if cont == quantidade:
        r1 = int(input('Deseja continuar??\n'
                       '(1) - Sim\n'
                       '(2) - Não\n'))
        while r1 != 1 and r1 != 2:
            r1 = int(input('Resposta inválida.Deseja continuar??\n'
                           '(1) - Sim\n'
                           '(2) - Não\n'))

        if r1 == 1:
            quantidade = int(input('Quantos valores a mais deseja digitar??  '))
            cont = 0
        else:
            break
lista = list(lista)
lista.sort()
print(f'Os valores adicionados foram: {lista}')