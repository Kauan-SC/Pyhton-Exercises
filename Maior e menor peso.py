# Solicitação de entrada
print('Analise de pesos!!')
Pessoas = input('Insira quantas pessoas vão ser analisadas:  ')
Peso_menor = None
Peso_maior = None
Media = 0

try:  # Verificação se o valor inserido é um número inteiro
    Pessoas = int(Pessoas)
    for c in range(1, Pessoas + 1):
        Peso = input(f'Insira o pessoa da pessoa {c}:  ')
        try:  # Verificação se o valor inserido é um número real
            Peso = float(Peso)
            Media += Peso

            if Peso_maior is None or Peso > Peso_maior:
                Peso_maior = Peso

            if Peso_menor is None or Peso < Peso_menor:
                Peso_menor = Peso

        except ValueError:
            print('Apenas valores reais são válidos!!')

    Media = Media / Pessoas
    print(f'O maior peso é de {Peso_maior} Kgs\n'
          f'O menor peso é de {Peso_menor} Kgs\n'
          f'A média é de {Media} Kgs')

except ValueError:
    print('Apenas valores inteiras são válidos!!')
