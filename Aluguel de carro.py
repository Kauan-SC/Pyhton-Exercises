# Solicitação de entrada
Dias = int(input('Quantos dias o carro ficou alugado?? '))
Km = float(input('Quantos km foram rodados?? '))

# Verificação de valores positivos
if Dias < 0 or Km < 0:
    print('Os valores precisam ser positivos!!')
else:

    # Calculo dos valores
    Soma1 = Dias * 60
    Soma2 = Km * 0.15
    Valor_final = Soma1 + Soma2

    # Exibição dos resultados
    print(f'Por {Dias} dias e {Km} quilometros rodados o cliente pagará R${Valor_final}!!')

