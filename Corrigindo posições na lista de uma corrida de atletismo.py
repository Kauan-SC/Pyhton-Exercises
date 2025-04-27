# Corrigindo posições na lista de uma corrida de atletismo

corrida = ["João", "Maria", "Pedro", "Ana"]

print("\nLista de corrida:  ")
for lista in corrida:
    print(lista, end=", ")

confirmacao = int(input(("\nA lista está correta? (1 - Sim, 2 - Não):  "))) # Confirmando se os nomes estão corretos
if confirmacao != 1:
    nome_incorreto = input("Digite o nome que está incorreto:  ")

    while True:
        if nome_incorreto in corrida:
            posicao: int = corrida.index(nome_incorreto)
            corrida.remove(nome_incorreto)
            break
        else:
            print("Esse nome não está na lista!!")
            sair = input("Deseja sair? (S/N):  ").upper()
            if sair == "S":
                exit()
            else:
                nome_incorreto = input("Digite o nome que está incorreto:  ")


    nome_correto = input("Digite o nome correto da pessoa:  ")
    corrida.insert(posicao, nome_correto)

    print("\nLista de corrida corrigida:  ")
    for lista in corrida:
        print(lista, end=", ")


