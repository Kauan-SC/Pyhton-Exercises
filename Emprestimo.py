# Solicitação de entrada
Emprestimo = input('Insira o valor do financiamento da casa R$')
Salario = input('Insira quanto você ganha por mês R$')
Anos = input('Em quantos anos você deseja pagar R$')

# Verificação de número
try:
    Emprestimo = float(Emprestimo) # Esses codigos checam se oque foi escrito foi uma letra ou número
    Salario = float(Salario)
    Anos = float(Anos)

    # Checando aprovação ou recusa de financiamento
    Conta1 = Anos * 12
    Pagamento_mensal = Emprestimo / Conta1
    Salario30 = Salario * 0.3
    Salario_Necessario = Pagamento_mensal / 0.3

    if Pagamento_mensal > Salario30:
        print(f'Você quer um financiamento de R${Emprestimo} reais, seu salário é de R${Salario} reais.')
        print(f'As parcelas do empréstimo vão ser no valor de R${Pagamento_mensal:.2f} reais.')
        print('Infelizmente, seu empréstimo foi recusado. Salário abaixo do necessário.')
        print(f'O salário necessário para esse empréstimo é de R${Salario_Necessario:.2f} reais.')

    else:
        print(f'Você quer um financiamento de R${Emprestimo} reais, seu salário é de R${Salario} reais.')
        print(f'As parcelas do empréstimo vão ser no valor de R$a{Pagamento_mensal:.2f} reais.')
        print('Seu empréstimo foi aprovado. Parabéns!')

except ValueError:
    print('Apenas números são permitidos!')
