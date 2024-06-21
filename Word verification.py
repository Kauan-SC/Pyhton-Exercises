# Entrace solicitacion
Sentence = str(input('Write any sentence: '))

# Sentence Verification
print('The letter A appears', Sentence.lower().count('a'), 'times!')

# Where
print('The first letter is in:', Sentence.find('a'), 'position!')
print('The last letter is in:', Sentence.rfind('a'), 'position!')
