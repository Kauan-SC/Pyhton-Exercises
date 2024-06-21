# Solicitação de entrada
Largura_Parede = float(input('Qual a largura da sua parede?? '))
Altura_Parede = float(input('Qual a altura da sua parede?? '))

# Verificação de valor positivo
if Largura_Parede < 0:
    print('Valor inválido')
if Altura_Parede < 0:
    print('Valor inválido')

# Conversão de valores
Metro_Quadrado = Largura_Parede*Altura_Parede
Eficiencia_Pintura = Metro_Quadrado/2.0

# Exibição dos resultados

print(f'Você precisará de exatamente {Eficiencia_Pintura: .2f} litros de tinta')