brasileirao = ('Botafogo', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Cruzeiro', 'São Paulo', 'Bahia', 'Athletico-PR',
               "RB Bragantino", 'Atlético-MG', 'Vasco', 'Juventude', 'Internacional', 'Grêmio', 'Fluminense',
               "Corinthians", 'Cuiabá', 'Santos', 'Goiás', 'Avaí')
print('#__# ' * 10)
print(f'{"Campeonato Brasileiro".center(50)}')
print('#__# ' * 10)

print('\nLista do G5:\n'
      f'{brasileirao[:5]}')

print('\nLista do Z4:\n'
      f'{brasileirao[-4:]}')

lista = brasileirao
lista = list(lista)
lista.sort()
print('\nOrdem alfabética:\n'
      f'{lista}')

print(f'\nA equipe do Bahia está na posição {brasileirao.index('Bahia')}')
