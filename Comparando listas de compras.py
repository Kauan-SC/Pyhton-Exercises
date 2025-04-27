# Comparando listas de compras

compras_aline = {"Batata", "Jilo", "Macarrão", "Café"}
compras_valeria = {"Arroz", "Feijão", "Macarrão", "Carne"}

compras_comuns = compras_aline.intersection(compras_valeria)
print(f"Compras comuns entre as duas listas: {', '.join(compras_comuns)}")

diferenca = compras_aline.difference(compras_valeria)
print(f"Compras exclusivas da Aline: {', '.join(diferenca)}")

diferenca = compras_valeria.difference(compras_aline)
print(f"Compras exclusivas de Valeria: {', '.join(diferenca)}")