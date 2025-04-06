# Introdução dos dados
site = str(input("Digite o site:  "))

if site[:8] == "https://" and site[-4:] == ".com":
    print("Site válido")
else:
    print("Site inválido")
