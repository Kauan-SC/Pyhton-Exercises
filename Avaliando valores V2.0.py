# Solicitação de entrada
valor = int(input('Digite um valor:  '))
cont = 1
soma = 0
numeros = []

while True:  # Lógica da avaliação
    numeros.append(valor)
    escolha = str(input('Você deseja continuar??  [S/N]  ').upper())
    if escolha == 'N':  # Se a escolha for Não, ele finaliza o loop
        soma += valor
        break
    elif escolha != 'S':  # Se a escolha for outra letra ele inválida a resposta
        escolha = str(input('Por favor, insira uma das duas opções: [S/N]  ').upper())
        soma += valor
        if escolha != 'S':
            break
        else:
            pass
    else:  # Resposta Sim para continuar
        cont += 1
        soma += valor
        valor = int(input('Digite um valor:  '))

media = soma / cont
maior = max(numeros)
menor = min(numeros)
print(f'Foram escritos {cont} números, a média é {media}\n'  # Resultado
      f'O maior número é {maior}, o menor número é {menor}')
