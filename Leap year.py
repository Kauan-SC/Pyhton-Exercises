# Entrace solicitacion
Year = input('Choose and write any year:  ')

# Number verification
try:
    Year = int(Year)
    Test = Year

    # Leap year verification
    if Test % 4 == 0 and ( Test % 100 != 0 or Test % 400 == 0):
        print(Year,'is a leap year!')
    else:
        print(Year,'is not a leap year!')

except ValueError:
    print('Only numbers are valid!')

