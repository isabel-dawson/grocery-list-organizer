# grocery-list-organizer
You can put in your grocery list, and then it reorganizes it by section at Wegmans

import random
random=random.randint (0,2500)
attempts = 0
print("Hello! What is your name? ")
name=str(input())
print("Okay, %s, I'm thinking of a number between 0 and 2500. You have three guesses." % name)
while attempts < 3:
    guess = int(input("Guess: "))
    if(guess == random):
        print("Congratulations! You win!")
        break
    else:
        print("Guess again!")
        attempts += 1
else:
    print("You lose, thanks for playing! " + "The correct number was " + str(random))



