import sys
import random

start = 5
end = 10




#Introduction
# print('\n***********\nHello World \n***********\n')
# print("Lets play a little game...")
# print("This game will determine if you are a genius or... not\n***********")
# print("The name of the game is guesse the number....")
# print("\nLets begin...")
# print(f"You have chosen to guesse between the numbers {start} and {end}")

#-----------------------------------------------------------------------

def guesse_the_number(guesse, answer):
    if guesse < start or guesse > end:
        print ("Oh no!\nSorry that is out of your choosen range.  Idiot\n")
        return
    if guesse == answer:
        print("You sir are a genius - you have won the game.  Goodbye!")
        return True
    if guesse != answer:
        print('Trump says, "wrong!"')
        return

if __name__ == '__main__':
    answer = random.randrange (start,end)
    # print(f'\n\nthis is the answer and is only here for testing purposes:  {answer} - DELETE ME')      #DONT FORGET TO DELETE ME 
    # print(type(answer))
    while True:
        try:
            guesse = int(input('Take a guess at what this number may be:'))
            if (guesse_the_number(guesse, answer)):
                break

        except ValueError:
            print(f'Oh no!\nPlease enter a number between {start} and {end}\n')
            continue

