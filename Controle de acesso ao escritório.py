# Introdução dos dados
nome = input("insira seu nome:  ")
cargo = input("insira seu cargo:  ")
horario = int(input("insira seu horário de entrada(24hrs):  "))

# Processando dados
if cargo == 'Estagiario':
    if 4 <= horario < 8:
        print(f"Ola {nome}")
        print("Chegou cedo, parabéns!!\n"
              "Acesso permitido.")
    elif 8 <= horario < 9:
        print(f"Ola {nome}")
        print("Acesso permitido.")
    elif 9 <= horario < 12:
        print(f"Ola {nome}")
        print("Você se atrasou, mais atenção!!\n"
              "Acesso permitido.")
    elif 12 <= horario < 18:
        print(f"Ola {nome}")
        print("Super atrasado!!"
              "Acesso negado.")
    elif 18 <= horario < 24 or horario < 4:
        print(f"Ola {nome}")
        print("Estamos fechados, voltei mais tarde!!")
    else:
        print("Insira um horário válido.")
if cargo == 'Gerente':
    if 4 <= horario < 12:
        print(f"Ola {nome}")
        print("Chegou cedo, parabéns!!\n"
              "Acesso permitido.")
    elif 12 <= horario < 18:
        print(f"Ola {nome}")
        print("Boa tarde!!"
              "Acesso permitido.")
    elif 18 <= horario < 24 or horario < 4:
        print(f"Ola {nome}")
        print("Estamos fechados, voltei mais tarde!!")
    else:
        print("Insira um horário válido.")

if cargo == 'Motorista':
    if 4 <= horario < 12:
        print(f"Ola {nome}")
        print("Você ira carregar carne!!\n"
              "Acesso permitido.")
    elif 12 <= horario < 18:
        print(f"Ola {nome}")
        print("Você ira carregar frango!!"
              "Acesso permitido.")
    elif 18 <= horario < 24 or horario < 4:
        print(f"Ola {nome}")
        print("Você ira carregar peixe!!\n"
              "Acesso permitido")
    else:
        print("Insira um horário válido.")
