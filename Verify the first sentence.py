# Entrace Solicitacion
City = str(input('Write a name of a city: '))

# City verification
if not City.replace(' ','').isalpha():
    print('Write a valid city!!')
else:

    # Correct name city verification
    City = City.lower()
    Correct = City.split()
    Word = 'santos'
    if Word in Correct:
        print('The city name is correct!!')
    else:
        print('Your answer is incorrect!!')
