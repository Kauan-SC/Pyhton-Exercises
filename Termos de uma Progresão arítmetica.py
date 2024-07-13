# Solicitação de entrada
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
Inicial = input('Termo inicial: ')
Razao = input('Razão: ')
Soma_final = Inicial

# Verificação de resposta
try:
    Inicial = int(Inicial)
    Razao = int(Razao)
    Soma_final = int(Soma_final)

    # Lógica da Progressão Aritmética
    print('Termos da PA:')
    for c in range(10):
        print(Soma_final, end=' -> ')
        Soma_final += Razao

    print('FIM')  # Para indicar o final da sequência

except ValueError:
    print('Apenas valores inteiros são permitidos!!')


