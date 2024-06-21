import random

# Solicitação de entrada
a1 = input('Qual o nome do aluno: ')
a2 = input('Qual o nome do aluno: ')
a3 = input('Qual o nome do aluno: ')
a4 = input('Qual o nome do aluno: ')
a5 = input('Qual o nome do aluno: ')
a6 = input('Qual o nome do aluno: ')
a7 = input('Qual o nome do aluno: ')

# Exibição de resultados
Lista = [a1,a2,a3,a4,a5,a6,a7]
random.shuffle(Lista)
print('A ordem será;\n')
print(Lista)

