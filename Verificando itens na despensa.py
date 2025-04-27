# Verificando itens na despensa
despensa = ["Arroz", "Feijão", "Macarrão", "Carne", "Leite", "Ovo", "Queijo", "Pão", "Salada", "Café"]
compras =  ["Batata", "Maionese", "Café"]

item = str(input("Qual item deseja verificar??\n"))

if item in despensa:
    print("Já temos esse item!!\n")
else:
    print("Adicionando a lista de compras!!\n")
    compras.append(item)
    print("Lista de compras atualizada:\n", compras)