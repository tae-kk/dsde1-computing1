print("what is your name?")
name = input("Enter name:")
print('hi ' + name)
print ("Guess a number between 1 and 10")
guess = input("Enter number:")
guess = int(guess)
import random
y = random.randint(1,10)
if y == guess:
    print("Hurrah! the answer was " + str(y))
else:
    print("No match, try again")
    guess = input("Enter number:")
    guess = int(guess)
    if y == guess:
        print("Hurrah!! the answer was " + str(y))
    else: 
        print("Nope, one last time")
        guess = input("Enter number:")
        guess = int(guess)
        if y == guess:
            print("Hurrah!!!")
        else:
            print("give up loser. the answer was " + str(y))
        

