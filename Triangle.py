# Entrace solicitacion
N1 = input('We are trying to form a triangle. Write a number:  ')
N2 = input('Write another number:  ')
N3 = input('Write another number:  ')

# Number verification
try:
    N1 = int(N1)
    N2 = int(N2)
    N3 = int(N3)

    # Result
    if (N1 + N2) > N3 and (N1 + N3) > N2 and (N2 + N3) > N1:
        print('We can form a triangle!')
    else:
        print('We cannot form a triangle!')

except ValueError:
    print('Only numbers are valid!')