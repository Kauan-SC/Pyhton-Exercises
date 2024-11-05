# Variáveis
dados = {}
lista = list()
mulheres = list()
m_soma = 0
soma_idades = 0
pessoas = 0
acima = list()

# Solicitação de entrada + Lógica do sistema
while True:
    dados['nome'] = str(input('Nome: '))
    pessoas += 1  # Conta quantidade de pessoas

    while True:  # Loop caso a resposta não seja M ou F
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()

        if dados['sexo'] == 'F':  # Salva os nomes das mulheres do teste
            m_soma += 1
            mulheres.append(dados['nome'])

        if dados['sexo'] in ['F', 'M']:
            break
        else:
            print('Digite apenas M ou F.')

    dados['idade'] = int(input('Idade: '))
    soma_idades += dados['idade']  # Soma a idade dos participantes

    continuar = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break

    lista.append(dados.copy())  # Salvando os dados em um lista


# Média das idades
media_idade = soma_idades / pessoas

# Idades acima da média
for pessoa in lista:
    if pessoa['idade'] >= media_idade:
        acima.append(pessoa['nome'])

# Resultado
print(f'{pessoas} foram entrevistadas!!')
print(f'Tivemos {m_soma} mulheres, que são: {", ".join(mulheres)}')
print(f'A soma das idades é: {soma_idades}')
print(f'A média das idades é: {media_idade:.2f}')
print(f'As pessoas com idade acima da média são: {", ".join(acima)}')