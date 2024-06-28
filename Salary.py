# Entrace solicitacion
Salary = input('How much do you earn per week?  ')

# Number verification
try:
    Salary = float(Salary)

    # Salary adjustment
    if Salary > 1250:
        F_Money = Salary + (Salary * 0.1)
    else:
        F_Money = Salary + (Salary * 0.15)

    # Result
    print('Now you will earn', F_Money,'per week!')

except ValueError:
    print('Only numbers are valid!')