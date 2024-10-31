# Solicitação de entrada
print(('=_=' * 8) + 'Sistema de notas' + ('=_=' * 8))
valor = int(input('Digite quantos dados vai inserir:  '))
total = []
media = []

# Salvando os dados inseridos
for i in range(valor):
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    total.append([nome, nota1, nota2])  # Salva os dados em uma string
    n = (nota1 + nota2) / 2
    media.append(n)  # Salva a média de cada aluno

# Resultado
print('#' * 30)
print(('N.'.ljust(5)) + 'Nome'.center(15) + ('Média'.rjust(8)))
for i in range(valor):
    print((f'{i+1:^5}'.ljust(5)) + f'{total[i][0]:^6}'.center(15) + f'{media[i]:^5}'.rjust(8))

print('\n')
for i in range(valor):
    print(' '.join(map(str, total[i])))
print()
