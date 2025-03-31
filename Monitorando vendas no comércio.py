# Solicitação de entrada
macas = int(input("Quantas maçãs foram vendidas??  \n"))
bananas = int(input("Quantas bananas foram vendidas??  \n"))

# Calculando o total vendido
total_vendido = macas + bananas

if macas > bananas:
    diferenca = macas - bananas
    print("Você vendeu mais maçãs que bananas!!\n")
    print(f"Diferença: {diferenca} maçãs")
elif bananas > macas:
    diferenca = bananas - macas
    print("Você vendeu mais bananas que maçãs!!\n")
    print(f"Diferença: {diferenca} bananas")
else:
    print("Você vendeu a mesma quantidade de maçãs e bananas!!\n")


