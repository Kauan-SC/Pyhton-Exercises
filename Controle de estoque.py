# Introdução de dados
estoque = 10
while estoque > 0:
    vendas = int(input("Quantos livros foram vendidos??\n"))
    estoque = estoque - vendas
    print(f"Estoque = {estoque}")

print(("Estoque esgotado!!"))