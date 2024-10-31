# Solicitação de entrada
print(('#_#' * 5) + 'Par e Impar' + ('#_#' * 5))
Quant = int(input('Quantos valores deseja inserir??  '))
Numeros = list()
Par = list()
Impar = list()
a = 1;

# Lógica
while a <= Quant:
    Valor = int(input('Digite um valor: '))
    Numeros.append(Valor)
    a += 1

# Resultado
Numeros.sort()
for i in Numeros:
    if i % 2 == 0:
        Par.append(i)
    else:
        Impar.append(i)

print(f'Os valores Pares digitados foram: {Par}')
print(f'Os valores Impares digitados foram: {Impar}')
