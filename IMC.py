# Introdução dos dados
peso = float(input("insira seu peso(KG):  "))
altura = float(input("insira sua altura(M):  "))

# Calculando o IMC
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso!!")
    print(imc)
elif 18.5 <= imc < 25:
    print("Peso normal!!")
    print(imc)
elif 25 <= imc < 30:
    print("Acima do peso!!")
    print(imc)
else:
    print("Calma lá paizão")
    print(imc)