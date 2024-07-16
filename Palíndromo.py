# Solicitação de entrada
print('Digite uma frase e vou te dizer se ela é um palíndromo ou não!!')
Frase = str(input('A frase é:  '))

Frase = Frase.replace(' ','')  # Lógica para eliminar os espaços e ficar mais fácil de identificar um palíndrom
Frase_invertida = Frase[::-1]
if Frase_invertida == Frase:  # Resultado
    print('Essa frase é um Palíndromo!!')
else:
    print('Essa frase não é um palíndromo\n'
          '',Frase_invertida)