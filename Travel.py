# Entrace solicitacion
Travel = input('Tell me the distance in kilometers that you will travel:  ')

# Number verification
try:
    Travel = float(Travel)

    if Travel < 0:
        print('This distance is impossible!')
    elif Travel < 0 and Travel <= 200:
        Result = Travel * 0.5
        print('You pay 0.5 dollars per kilometer')
        print('Your travel will cost $', Result)
    else:
        Result = Travel * 0.45
        print('You pay 0.45 dollars by the Km')
        print('Your travel will cost $',Result)

except ValueError:
    print('Only numbers are valid.Change your answer!')
