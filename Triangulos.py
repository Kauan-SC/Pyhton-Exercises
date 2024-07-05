# Solicitação de entrada
print('Vamos criar um triangulo!!')
L1 = input('Insira o valor de um dos lados:  ')
L2 = input('Insira o valor de outro lado:  ')
L3 = input('Insira o valor do ultimo lado:  ')

# Verificação das respostas
try:
    L1 = int(L1)
    L2 = int(L2)
    L3 = int(L3)

    if (L1 + L2) > L3 and (L2 + L3) > L1 and (L1 + L3) > L2:
        print('Os valores inseridos formam um triangulo!')

        # Triangulo Escaleno, Isósceles e Equilátero
        if L1 == L2 == L3:
            print('Esse é um triangulo equilátero.Pois contém todos os lados iguais!')
        elif L1 == L2 or L2 == L3 or L1 == L3:
            print('Esse é um triangulo Isósceles.Pois contém dois lados iguais e um diferente!')
        elif L1 != L2 and L2 != L3:
            print('Esse é um triangulo Escaleno.Pois contém todos os lados diferentes!!')
        else:
            print('ERROR')

    else:
        print('Esses valores não formam um triangulo, por favor escolha outros números!')

except ValueError:
    print('Apenas números inteiros são válidos!')
