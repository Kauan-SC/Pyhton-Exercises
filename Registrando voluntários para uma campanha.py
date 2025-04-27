# Registrando voluntários para uma campanha

voluntários = []
while True:
    nome = input("Digite o nome do voluntário:  ")

    if nome == "FIM":
        break

    voluntários.append(nome)

print("\nLista de voluntarios:  ")
for voluntario in voluntários:
    print(voluntario)