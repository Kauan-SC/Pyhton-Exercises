# Solicitação de entrada
print('='*20)
dicionario = {}
dicionario['nome'] = str(input('Digite o nome do aluno: '))  # Pegando o nome e salvando no dicionário
dicionario['media'] = float(input('Digite a média do aluno:  '))  # Pegando a média e salvando no dicionário

# Aprovado ou Reprovado
if dicionario['media'] >= 7:  # Verificação de aprovado ou reprovado
    dicionario['resultado'] = 'Aprovado'
else:
    dicionario['resultado'] = 'Reprovado'

# Resultado
print(f'Aluno: {dicionario["nome"]}')
print(f'Média: {dicionario["media"]}')
print(f'Situação: {dicionario["resultado"]}')