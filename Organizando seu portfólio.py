# Introdução dos dados
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for i in range(5):
    if projetos[i] is None:
        print(f"Projeto {i+1}: Não foi desenvolvido")
    else:
        print(f"Projeto {i+1}: {projetos[i]}")
