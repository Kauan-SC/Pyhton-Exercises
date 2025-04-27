# Introdução dos dados
import re

receita = str(input("Digite a receita:  "))

numeros = re.findall(r'\d+', receita)[0]

print(numeros)
