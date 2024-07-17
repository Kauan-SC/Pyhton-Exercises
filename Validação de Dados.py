# Solicitação de entrada
Sexo = input('Informe seu sexo [M/F]:  ').upper()

while Sexo != 'M' and Sexo != 'F':  # Lógica que refaz a pergunta até a resposta ser M ou F
    print('Dados inválidos.Por favor insira seu sexo:  ')
    Sexo = input('Informe seu sexo [M/F]:  ').upper()

print('Seu sexo foi salvo!!')
if Sexo == 'M':
    print('Você é do sexo masculino!!')
else:
    print('Você é do sexo feminino!!')