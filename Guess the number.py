import random

# Entrace solicitacion
print('I will think of a number between 0 and 5!')
Number = (input('What number am I thinking of?  '))

# Number verification
if not Number.isdigit():  # Validation if it´s a number or not
    print('Only numbers are valid!')
else:
    Number = int(Number)  # Changing the answer to a int number

    if Number < 0 or 5 < Number:  # Validation if the answer it´s between 0 and 5
        print('Please,write a number between 0 and 5!')
    else:

        # Random number
        Random = random.randint(0,5)  # Randomazing the answer from computer

        # Result
        if Random == Number:
            print('You win!!')
            print('The number I chose is:',Random)
        else:
            print('You lose!')
            print('The number I chose is:', Random)