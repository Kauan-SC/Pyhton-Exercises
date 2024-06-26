# Entrace solicitacion
Speed = input('Tell me what´s yours speed:  ')

# Number verification
if Speed.isalpha():  # Validation if it´s a number or not
    print('Only numbers are valid!')
else:
    Speed = float(Speed)

    # Result for high,low and invalid speed
    if Speed < 0:  # Checking if the answers it´s not a negative number
        print('This speed it´s invalid.Please, enter a valid number!')
    else:

        if Speed > 0 and Speed < 80:  # Checking if the car it´s in the correct speed
            print('Thanks!! Have a good trip.')
        else:
            Fine = 7 * (Speed - 80)  # Applying the fine
            print(f'You have exceeded the speed limit. Your fine will be ${Fine:.2f} dollars.')
