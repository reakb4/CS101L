########################################################################
##
## CS 101 Lab
## Program #4
## Name Raney Adams
## Email - reakb4@umsystem.edu
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random

def play_again(play) -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and 
True if Y or YES.  Keeps asking until they respond yes '''
    play = 'a'
    while play != 'NO' or play != 'N' or play != 'Yes' or play != 'Y':
        play = input('Do you want to play again:\n')
        play = play.upper()
        if play == 'YES' or play == 'Y':
            return True
        elif play == 'NO' or play == 'N':
            return False
        else:
            print('You must enter Y/YES/N/NO. Please try again.')
            continue
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is 
<= 0 or greater than the amount they have '''
    amount = int(input('How many chips do you want to wager?'))
    while amount <= 0 or amount > bank:
        if amount <= 0:
            print('The wager cant be less than or equal to 0. Please try again.')
        if amt_chips > 100:
            print('The wager cant be greater than the 100. Please try again.')
        amount = int(input('Enter the amount you want to wager:\n'))
    return amount
        
def get_slot_results(a,b,c) -> tuple:
    ''' Returns the result of the slot pull '''
    a = random.radint(1,10)#gets random number between 1-10
    b = random.radint(1,10)#gets random number between 1-10
    c = random.radint(1,10)#gets random number between 1-10
    return a, b, c

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb and reela == reelc:
        return 3
    if reela == reelb and reela != reelc:
        return 2
    if reela != reelb and reela == reelc:
        return 2
    if reelb == reelc and reela != reelc:
        return 2
    if reela != reelb and reela != reelc:
        return 0
    
def get_bank(amount) -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value 
greater than 0 and less than 101 '''
    amount = 0
    while amount <=0 or amount > 100:
        amount = int(input('How many chips do you want to play with?\n'))#gets entered amount
        if amount <= 0:#checks if amount is within bounds, if not repeats
            print('Amount too low, the number needs to be between 1-100. Try again.')
            continue#resets loop since value is outside of bounds
        elif amount > 100:#checks if amount is within bounds, if not repeats
            print('Amount too high, the number needs to be between 1-100. Try again.')
            continue#resets loop since value is outside of bounds
    return amount

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times 
the wager if 2 match, and negative wager if 0 match '''
    if matches == 0:#profit for 0 matches based on wager
        profit = wager * -1
    elif matches == 2:#profit for 2 matches based on wager
        profit = wager * 3 - wager
    elif matches == 3:#profit for 3 matches based on wager
        profit = wager *10 - wager
    return profit

if __name__ == "__main__":
    
    playing = True
    while playing:
        
        bank = get_bank()

        while bank > 0: #Replace with condition for if they still have money.

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
