# Entrace solicitacion
N1 = input('Write a number:  ')
N2 = input('Write another number:  ')
N3 = input('Write another number:  ')

# Number verification
try:
    N1 = float(N1)
    N2 = float(N2)
    N3 = float(N3)

    # Greater verificaion
    if N1 > N2 and N1 > N3:
        Greater = N1
    elif N2 > N1 and N2 > N3:
        Greater = N2
    else:
        Greater = N3

    # Less verification
    if N1 < N2 and N1 < N3:
        Less = N1
    elif N2 < N1 and N2 < N3:
        Less = N2
    else:
        Less = N3

    # Result
    print('The greatest number is:',Greater)
    print('The smallest number is:',Less)

except ValueError:
    print('Only numbers are valid!')