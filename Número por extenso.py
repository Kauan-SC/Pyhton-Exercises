# Solicitação de entrada
valor = int(input('Digite um valor entre 0 e 20:  '))
v2 = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

while valor < 0 or valor > 20:
    valor = int(input('Tente novamente.Digite um valor entre 0 e 20:  '))

print(f'Você escolheu o número {v2[valor]}')
