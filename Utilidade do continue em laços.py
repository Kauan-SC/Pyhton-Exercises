# introdução dos dados
livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for i in range(5):
    if livros[i]["estoque"] > 0:
        print("Nome:", livros[i]["nome"])
        print("Estoque:", livros[i]["estoque"])
        print("")
    