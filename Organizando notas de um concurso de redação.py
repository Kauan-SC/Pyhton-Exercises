# Organizando notas de um concurso de redação

alunos = []

while True:
    nome = str(input("Digite o nome do aluno:  "))
    nota = float(input("Digite a nota do aluno:  "))
    alunos.append([nome,nota])

    continuar = str(input("Deseja continuar? (S/N):  ")).upper()
    if continuar != "S":
        break

print("\nLista de classificação:")
alunos.sort(key=lambda x: x[1], reverse=True)
for aluno in alunos:
    print(f"Aluno: {aluno[0]}, Nota: {aluno[1]}")