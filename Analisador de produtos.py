# Solicitação de entrada
print('-' * 15)
print('     CAIXA')
print('-' * 15)
produtos = []
valores = []
cont_1000 = 0

while True:
    produto = str(input('\nInsira o nome do produto:  '))
    print('-' * 30)
    valor = float(input('Insira o valor do produto:  '))
    print('-' * 30)
    if valor > 1000:
        cont_1000 += 1
        produtos.append(produto)  # Armazenamento em lista de todos os produtos e valores
        valores.append(valor)
    else:
        produtos.append(produto)  # Armazenamento em lista de todos os produtos e valores
        valores.append(valor)

    while True:
        programa = input('Mais algum produto?? [S/N] ').upper()
        print('-' * 30)
        if programa == 'S':
            break
        elif programa == 'N':
            # Se o usuário responde 'N', saímos do loop principal
            break
        else:
            print('Resposta inválida. Por favor, responda com "S" para sim ou "N" para não.')

    if programa == 'N':
        break


if valores:
    menor_valor = min(valores)
    maior_valor = max(valores)

    pmenorv = produtos[valores.index(menor_valor)]
    pmaiorv = produtos[valores.index(maior_valor)]

    soma_compra = sum(valores)
    print(f'O valor final dos produtos é R${soma_compra}\n'
          f'Existem {cont_1000} produtos com o valor acima de R$1000,00\n'
          f'O produto mais barato é {pmenorv}, a {menor_valor}\n'
          f'O produto mais caro é {pmaiorv}, a {maior_valor}')

else:
    print('Nenhum valor foi inserido!!')