# Solicitação de entrada
Preco = input('Insira o valor das compras: R$')

print(('=' * 10) + 'FORMAS DE PAGAMENTO' + ('=' * 10))
Pagamento = input('(1) Pagamento à vista dinheiro/cheque\n'
                  '(2) Pagamento à vista cartão de débito\n'
                  '(3) Pagamento à vista no cartão de crédito\n'
                  '(4) Pagamento parcelado no cartão de crédito\n'
                  'Escolha a forma de pagamento: ')

# Verificação de respostas
try:
    Preco = float(Preco)
    try:
        Pagamento = int(Pagamento)
        if Pagamento == 1:
            Valor_final = Preco - (Preco * 0.1)
            print('O desconto no dinheiro/cheque à vista é de 10%')
            print(f'O valor final a ser pago com desconto é de R${Valor_final:.2f}')
        elif Pagamento == 2:
            Valor_final = Preco - (Preco * 0.05)
            print('O desconto no cartão de débito à vista é de 5%')
            print(f'O valor final a ser pago com desconto é de R${Valor_final:.2f}')
        elif Pagamento == 3:
            Valor_final = Preco - (Preco * 0.02)
            print('O desconto no cartão de crédito à vista é de 2%')
            print(f'O valor final a ser pago com desconto é de R${Valor_final:.2f}')
        elif Pagamento == 4:
            Valor_dividido = Preco + (Preco * 0.2)
            print(('=' * 10) + 'FORMAS DE DIVISÃO' + ('=' * 10))
            print(f'Dividido em 2x: {Preco / 2:.2f}\n'
                  f'Dividido em 3x: {Valor_dividido / 3:.2f}\n'
                  f'Dividido em 4x: {Valor_dividido / 4:.2f}\n'
                  f'Dividido em 5x: {Valor_dividido / 5:.2f}\n'
                  f'Dividido em 6x: {Valor_dividido / 6:.2f}\n'
                  f'Dividido em 7x: {Valor_dividido / 7:.2f}\n'
                  f'Dividido em 8x: {Valor_dividido / 8:.2f}\n'
                  f'Dividido em 9x: {Valor_dividido / 9:.2f}\n'
                  f'Dividido em 10x: {Valor_dividido / 10:.2f}')

            Forma = input('Escolha em quantas vezes deseja pagar: ')
            try:
                Forma = int(Forma)
                if Forma == 2:
                    print(f'O valor a ser pago é de R${Preco / 2:.2f} em {Forma}x vezes!!')
                elif 3 <= Forma <= 10:
                    print(f'O valor a ser pago é de R${Valor_dividido / Forma:.2f} em {Forma}x vezes')
                else:
                    print('Quantidade de parcelas inválidas!!')
            except ValueError:
                print('Quantidade de parcelas inválida!!')

        else:
            print('Escolha inválida!!')
    except ValueError:
        print('Forma de pagamento inválida!!')

except ValueError:
    print('Apenas valores reais são permitidos!!')
