# Solicitação de entrada
Valor_Produto = float(input('Qual o valor do produto? '))
Desconto = int(input('Qual o valor do desconto? '))

# Verificação de valores positivos
if Valor_Produto < 0 or Desconto < 0:
    print('Os valores precisam ser positivos')
else:
    # Cálculo do valor final
    Valor_Final = Valor_Produto - (Valor_Produto * (Desconto / 100))

    # Exibição dos resultados
    print(f'O produto vale {Valor_Produto} reais, ganhou desconto de {Desconto}%\n'
          f'O produto final equivale a {Valor_Final: .2f} reais!!')
