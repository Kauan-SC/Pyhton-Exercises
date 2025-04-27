# Unindo o relatório de estoques

estoque1 = ["Arroz", "Feijão", "Macarrão", "Carne", "Leite"]
estoque2 = ["Ovo", "Queijo", "Pão", "Salada", "Café", "Açúcar", "Sal"]

relatorio = estoque1 + estoque2
print(f"Lista de itens:  ")
for items in relatorio:
    print(items, end=", ")

