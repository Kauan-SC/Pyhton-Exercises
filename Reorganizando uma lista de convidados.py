# Reorganizando uma lista de convidados

convidados = ["João", "Maria", "Pedro", "Ana"]

novo_convidado = input("Digite o nome do novo convidado:  ")
lugar_convidade = int(input("Digite o número da lugar do convidado:  "))
convidados.insert(lugar_convidade - 1, novo_convidado)

print("\nLista de convidados:  ")
for lista in convidados:
    print(lista, end=", ")