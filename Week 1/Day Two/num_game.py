# HOT & COLD GAME
# Create a game where the range of numbers will be between 0-100
# Number of guesses = 10
# If user is within 5 of the winning number, print hot ( 5 & -5)
# If within 10, print warm (-10, 10)
# For everything else it will be cold
# Keep track of all the user guesses in a list

# When the game is over, print out the 
# 1 - number of tries the user took
# 2 - their guesses

import random

winning_number = random.randint(0,100)
print(winning_number)

total_guesses = 10
guesses = []
user_won = False
guesses_taken = 0

while guesses_taken < total_guesses and user_won != True:
    user_guess = int(input("Enter your guess: "))
    guesses.append(user_guess)    # adds user guess to the list
    guesses_taken += 1            # every single time user guesses, increment it by 1
    if user_guess == winning_number:
        user_won = True
        print("Congrats, you won!")

    elif user_guess >= winning_number - 5 and user_guess <= winning_number + 5:
        print("Hot")
    elif user_guess >= winning_number - 10 and user_guess <= winning_number + 10:
        print("Warm")
    else:
        print("Cold")

print("You took", guesses_taken, "guesses")
print("Your guesses were: ")
print(guesses)