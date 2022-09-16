print('Welcome to the Flarsheim Guesser!')
print()
print('Please think of a number between and including 1 and 100.')
print()

user_play = True
While (user_play):
    user = input('Do you want to play again? Y to continue, N to quit ==>')
    if (user_play == 'Y'):
        user_play = True
    if (user_play == 'N'):
        user_play = False
        break

user_remain3 = True
user_remain5 = True
user_remain7 = True

    while user_remain3:
        user_remain3 = int(input('What is the remainder when your number is divided by 3 ?'))
        if user_remain3 < 0:
        print('The value entered must be 0 or greater')
        elif user_remain3 > 3:
        print('The value entered must be less than 3')
        elif user_remain3 == 0:
        break
        elif user_remain3 == 1:
        break
        elif user_remain3 == 2:
        break

    while user_remain5:
        user_remain5 = int(input('What is the remainder when your number is divided by 5 ?'))
        if user_remain5 < 0:
            print('The value entered must be 0 or greater')
        elif user_remain5 > 5:
            print('The value entered must be less than 5')
        elif user_remain5 == 0:
            break
        elif user_remain5 == 1:
            break
        elif user_remain5 == 2:
            break
        elif user_remain5 == 3:
            break
        elif user_remain5 == 4:
            break
        elif user_remain5 == 5:
            break

    while user_remain7:
        user_remain7 = int(input('What is the remainder when your number is divided by 7 ?'))
        if user_remain7 < 0:
            print('The value entered must be 0 or greater')
        elif user_remain7 > 7:
            print ('The value entered must be less than 7')
        elif user_remain7 == 0:
            break
        elif user_remain7 == 1:
            break
        elif user_remain7 == 1:
            break
        elif user_remain7 == 2:
            break
        elif user_remain7 == 3:
            break
        elif user_remain7 == 4:
            break
        elif user_remain7 == 5:
            break
        elif user_remain7 == 6:
            break
        elif user_remain ==7:
            break






