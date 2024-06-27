# Entrace solicitacion
Number = input('Write a number and I will say if it is Even or Odd:  ')

# Number verification
try:
    Number = int(Number)

    # Even or Odd
    if Number % 2 == 0:
        print('This number is Even!')
    else:
        print('This number is Odd!')

except ValueError:
    print('Only integer numbers are valid!')