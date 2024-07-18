# Solicitação de entrada
print('=-=' * 10)
print('     Super Gerador de PA')
print('=-=' * 10)

n1 = int(input('\nInsira o primeiro termo:  '))
n2 = int(input('Insira o segundo termo:  '))
c = 1
termo = n1

while True:
    print(termo, ' -> ', end='')
    termo += n2

    escolha = int(input('\nVocê deseja continuar??\n'
                        '(1) - Sim\n'
                        '(2) - Não\n'))
    if escolha == 2:
        break
    elif escolha != 1:
        print('Valor inválido!!')
        break

print('Fim da PA!!')