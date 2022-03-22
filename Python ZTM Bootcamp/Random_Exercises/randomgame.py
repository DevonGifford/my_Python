import sys
import random

start = int(sys.argv[1])
end = int(sys.argv[2])

answer = random.randrange (start,end)
print(f'\n\nthis is the answer and is only here for testing purposes:  {answer} - DELETE ME')      #DONT FORGET TO DELETE ME 
print(type(answer))

#Introduction
print('\n***********\nHello World \n***********\n')
print("Lets play a little game...")
print("This game will determine if you are a genius or... not\n***********")
print("The name of the game is guesse the number....")
print("\nLets begin...")
print(f"You have chosen to guesse between the numbers {start} and {end}")

#-----------------------------------------------------------------------


while True:
    try:
        guesse = (int(input('Take a guess at what this number may be:'))) 
        if guesse < start or guesse > end:
            print ("Oh no!\nSorry that is out of your choosen range.  Idiot\n")
            continue
        if guesse == answer:
            print("You sir are a genius - you have won the game.  Goodbye!")
            break
    except ValueError:
        print(f'Oh no!\nPlease enter a number between {start} and {end}\n')
        continue



