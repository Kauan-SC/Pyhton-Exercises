# Introdução dos dados
dias = []

for i in range(3):
    dias.append(int(input("Digite quantos dias faltam:  \n")))
    if dias[i] < 0:
        print("Digite um número positivo!")
        dias[i] = int(input("Digite quantos dias faltam:  \n"))

for i in range(3):
    print(f"Na {i+1} posição, faltam {dias[i]} dias.")