# Entrace solicitacion

Name = str(input('Write a name: '))

# Name verification
if not Name.replace(' ','').isalpha():
    print('Write a valid name!')
else:

    # Name count result
    N = Name.split()
    print('The first name is:',N[0])
    print('The last name is:',N[len(N)-1])

