# Entrace solicitacion
Name = input('What´s your name?? \n')

# Uppercase and Lowercase name
print('Written in uppercase: ', Name.upper())
print('Written in lowercase: ', Name.lower())

# Count of letters
print('The number of letters with space is: ', len(Name))
print('The number of just letters is: ', len(Name.replace(' ', '')))

# First name
First = Name.split()
print('The first name is: ', First[0])
