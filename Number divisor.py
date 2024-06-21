# Entrace solicitacion
Number = str(input('Write any number between 0 and 9999: '))

# Number verification
if not Number.isdigit():
    print('Write a valid number')
elif len(Number) > 4:
    print('This number is invalid.Write a number between 0 a 9999!!')
else:

    # Number divisor result
    Number = Number.zfill(4)
    print('First ',Number[0])
    print('Second ',Number[1])
    print('Third ',Number[2])
    print('Fourth ',Number[3])
