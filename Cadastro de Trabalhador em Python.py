# Bibliotecas
import datetime

# Variáveis
dados = {}
ano_atual = datetime.date.today().year

# Título
print('='*40)
print('Cadastro de Trabalhador'.center(40))
print('='*40)

# Solicitação de entrada
dados['nome'] = str(input('Insira o nome: '))  # Guarda o nome do trabalhador
nascimento = int(input('Insira o ano de nascimento: '))
carteira = str(input('Você tem carteira de trabalho??(S/N) ').upper())

# Lógica para gerar dados caso carteira seja assinada
if carteira == 'S':
    dados['contratação'] = int(input('Insira o ano de contratação: '))  # Guarda dados sobre quando foi contratado
    dados['salario'] = float(input('Insira o salário:  '))  # Guarda o valor do salário
else:
    pass

# Descobrindo idade
dados['idade'] = ano_atual - nascimento

# Descobrindo aposentadoria
aposentado = dados['contratação'] + 35
idade_aposentado = dados['idade'] + 35

# Resultado final dos dados
print('='*40)
print(f'Nome - {dados["nome"]}')
print(f'Idade - {dados["idade"]}')
if carteira == 'S':
    print(f'Contratação - {dados['contratação']}')
    print(f'Salario - {dados["salario"]}')
    print(f'Você vai se aposentar em {aposentado}, com {idade_aposentado} anos!!')
else:
    print('Você não tem carteira de trabalho!!')