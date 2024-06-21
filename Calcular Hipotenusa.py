import math
# Solicitação de entrada
Cateto_adjacente = float(input('Qual o valor do primeiro cateto?? '))
Cateto_oposto = float(input('Qual o valor do segundo cateto?? '))

# Verificação de valores positivos
if Cateto_oposto < 0 or Cateto_adjacente < 0:
    print('Os valores precisam ser positivos!!')
else:

    # Calculo dos valores
    C = (Cateto_oposto ** 2) + (Cateto_adjacente ** 2)
    Hipotenusa = math.sqrt(C)

    # Exibição dos resultados
    print(f'O valor da hipotenusa é {Hipotenusa}!!')