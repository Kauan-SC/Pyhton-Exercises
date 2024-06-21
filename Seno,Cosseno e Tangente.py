# Solicitação de entrada
try:
    cateto_adjacente = float(input('Qual o valor do cateto adjacente? '))
    cateto_oposto = float(input('Qual o valor do cateto oposto? '))
    hipotenusa = float(input('Qual o valor da hipotenusa? '))

    # Verificação de valores positivos
    if cateto_adjacente <= 0 or cateto_oposto <= 0 or hipotenusa <= 0:
        print('Insira valores positivos!')
    else:
        # Cálculo das razões trigonométricas
        seno = cateto_oposto / hipotenusa
        cosseno = cateto_adjacente / hipotenusa
        tangente = cateto_oposto / cateto_adjacente

        # Exibição dos resultados
        print('-' * 10)
        print(f'Valor de Seno: {seno:.2f}')
        print(f'Valor de Cosseno: {cosseno:.2f}')
        print(f'Valor de Tangente: {tangente:.2f}')
        print('-' * 10)

except ValueError:
    print('Insira valores numéricos válidos!')

