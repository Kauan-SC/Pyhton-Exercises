# Solicitação de entrada
Salario_inicial = float(input('Qual o valor atual do salario do funcionario??R$'))
Aumento = int(input('Quanto de aumento ele irá receber(em %)?? '))

# Verificação de valores positivos
if Salario_inicial <0 or Aumento <0:
    print('Os valores precisam ser positivos')
else:
    # Calculo do salario final
    Salario_final = Salario_inicial + (Salario_inicial*(Aumento/100))

    # Exibição dos resultados
    print(f'O salario inicial é de {Salario_inicial}, o aumento é de {Aumento}%\n'
          f'O salario final será de {Salario_final}')