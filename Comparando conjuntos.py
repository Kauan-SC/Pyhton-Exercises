# Comparando conjuntos

letras1 = {"a", "b", "c", "d", "e"}
letras2 = {"f", "g", "h", "c", "a"}

remover = letras1.intersection(letras2)
conjunto = letras1.union(letras2)

for letra in remover:
    conjunto.remove(letra)

print(f"Conjunto de letras: {conjunto}")