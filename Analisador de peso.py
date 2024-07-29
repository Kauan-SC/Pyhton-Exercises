print('#' * 40)
print('ANALISADOR DE PESO'.center(40))
print('#' * 40)

cadastro = []
soma = 0

quantidade = int(input('Quantas pessoas serão cadastradas??  '))
for c in range(quantidade):
    nome = str(input('Insira o nome:  '))
    peso = int(input('Insira o peso:  '))
    cadastro.append([nome,peso])
    soma += peso

media = soma / quantidade
maior = max(cadastro, key=lambda x: x[1])
menor = min(cadastro, key=lambda x: x[1])
print(f'O número de pessoas cadastradas é de: {quantidade}')
print(f'Maior peso é {maior[1]}.De {maior[0]}')
print(f'Menor peso é {menor[1]}.De {menor[0]}')
print(f'A media dos pesos é {media}')

