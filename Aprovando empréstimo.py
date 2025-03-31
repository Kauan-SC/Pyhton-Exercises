# Introdução dos dados
salario = float(input("Insira o valor do seu salário:  "))
emprestimo = float(input("Insira o valor do empréstimo:  "))

# Validando o empréstimo
if emprestimo > salario * 0.3:
    print("Empréstimo não aprovado")
else:
    print("Empréstimo aprovado")
