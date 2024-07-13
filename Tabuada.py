# Solicitação de entrada
print('Vamos fazer a tabuada!!')
Numero = input('Escolha um número:  ')
Multiplicacao = input('Insira quantas vezes quer multiplicar o número:  ')
Soma_total = 0

try:
    Numero = int(Numero)  # Verificação se a resposta é um número inteiro
    Multiplicacao = int(Multiplicacao)  # Verificação se a resposta é um número inteiro
    for c in range(1, Multiplicacao+1):
        Tabuada = Numero * c  # Lógica e resultado
        Soma_total += Tabuada
        print(('#' * 4) + f' {Numero} X {c} = {Tabuada} ' + ('#' * 5))

    print(f'A soma total da tabuada é {Soma_total}')
except ValueError:
    print('Apenas números inteiros são validos!!')

