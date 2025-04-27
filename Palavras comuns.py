# Palavras comuns

texto1 = input("Digite um texto:  ")
texto2 = input("Digite outro texto:  ")

palavra = set(texto1.split())
palavra2 = set(texto2.split())

palavras_comuns = palavra.intersection(palavra2)
print("Palavras comuns entre os dois textos:", palavras_comuns)

