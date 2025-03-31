# Introdução dos dados
livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

livro_buscado = str(input("Digite o nome do livro que deseja buscar:  "))

for i in range(6):
    if livro_buscado == livros[i]:
        print(f"O livro {livro_buscado} está na posição {i+1} na lista.")
        break
    else:
        pass
if livro_buscado not in livros:
    print("O livro não foi encontrado na lista!!")
