# Faça como eu fiz: organizando uma lista de convidados

convidados = []

while True:
    convidados.append(input("Digite o nome do convidado:  "))
    continuar = input("Deseja continuar? (S/N):  ").upper()

    if continuar != "S":
        break

convidados = list(set(convidados))
print(convidados)
