# Removendo o último item de um pedido
pedido = ["Sanduiche", "Suco", "Cerveja", "Pão", "Refrigerante"]

while True:
    print("\nLista de itens:  ")
    for items in pedido:
        print(items, end=", ")

    pedido.pop()  # Removendo o último item da lista
    print("\n")

    if len(pedido) == 0:
        break
