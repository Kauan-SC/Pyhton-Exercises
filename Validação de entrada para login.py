# Introdução dos dados

nome = (str(input("Digite seu nome:  ")))
a = len(nome)
senha = (str(input("Digite sua senha:  ")))
b = len(senha)

while a < 5 and b < 8:
    print("Nome e senha inválidos")
    print("É necessário que o nome tenha 5 caracteres e a senha 8!!")

    nome = (str(input("Digite seu nome:  ")))
    a = len(nome)
    senha = (str(input("Digite sua senha:  ")))
    b = len(senha)