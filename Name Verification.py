# Entrace solicitacion
Name = str(input('Write a name: '))

# Name verification
if not Name.replace(' ','').isalpha():
    print('Write a valid name!')
else:

    # Correct name verification
    Name = Name.lower()
    Correct = Name.split()
    Word = 'silva'
    if Word in Correct:
        print('This name contains Silva!')
    else:
        print('This name does not contains Silva!')
