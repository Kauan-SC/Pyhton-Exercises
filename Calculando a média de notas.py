# Calculando a média de notas

notas = []

while True:
    nome = input("Digite o nome do aluno:  ")
    nota = float(input("Digite a nota final do aluno:  "))
    media = nota / 4
    notas.append([nome,nota,media])

    continuar = input("Deseja continuar? (S/N):  ").upper()
    if continuar != "S":
        break

print("\nLista de notas:  ")
notas.sort(key=lambda x: x[2], reverse=True)
for aluno in notas:
    print(f"Aluno: {aluno[0]}, Nota: {aluno[1]}, Média: {aluno[2]}")