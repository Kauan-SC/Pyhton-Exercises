# Solicitação de entrada
print('Vamos calcular o seu IMC')
Peso = input('Insira seu peso atual em kilogramas:  ')
Altura = input('Insira a sua altura atual em metros:  ')

# Verificação de respostas
try:
    Peso = float(Peso)
    Altura = float(Altura)

    # Lógica e resultado
    IMC = Peso / (Altura * Altura)
    if 0 < IMC < 18.5:
        print(f'Seu IMC foi de {IMC}, você está abaixo do peso!!')
    elif 18.5 <= IMC < 25:
        print(f'Seu IMC foi de {IMC}, você está no peso padrão!!')
    elif 25 <= IMC < 30:
        print(f'Seu IMC foi de {IMC}, você está em sobrepeso!!')
    elif 30 <= IMC < 40:
        print(f'Seu IMC foi de {IMC}, você está obeso!!')
    elif IMC >= 40:
        print(f'Seu IMC foi de {IMC}, você está em obesidade morbida!!')
    else:
        print('Valores inválidos!!')

except ValueError:
    print('Apenas números reais são válidos!!')
