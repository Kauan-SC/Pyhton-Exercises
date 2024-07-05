# Solicitação de entrada
print('Vamos calcular a média de notas dos alunos')
Contador = input('Insira quantas notas vão ser inseridas: ')

try:
    Contador = int(Contador)  # Converte o número de notas para inteiro
    N1 = 0
    Soma_Notas = 0  # Inicializa a soma das notas fora do loop

    # Contador de número de notas
    while N1 < Contador:
        Notas = input('Insira a nota: ')

        try:
            Notas = float(Notas)  # Converte a nota para float
            Soma_Notas += Notas  # Adiciona a nota à soma das notas
            N1 += 1
        except ValueError:
            print('Por favor, insira um número válido.')

    # Média
    Media = Soma_Notas / Contador
    print(f'Você inseriu {Contador} notas de provas\n'
          f'Sua nota total foi de {Soma_Notas:.3}, e sua média foi {Media:.3}!!')

    # Aprovado, recuperação ou reprovado
    if Media > 0 and Media <= 5:
        print('\nInfelizmente você foi reprovado!!')
    elif Media > 5 and Media < 7:
        print('\nVocê ainda tem uma chance, está de recuperação!!')
    elif Media >= 7 and Media <= 10:
        print('\nParabéns,você foi aprovado com sucesso!!')
    else:
        print('Média fora do padrão de notas.Verifique se as notas inseridas estão corretas"!!')

except ValueError:
    print('Apenas números inteiros são permitidos!!')
