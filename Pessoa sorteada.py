import random

# Solicitação de entrada
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')

# Exibição do resultado
Sequencia = [a4,a2,a3,a1]
Sorteado = random.choice(Sequencia)
print(f'O aluno sorteado é {Sorteado}!!')
