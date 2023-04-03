import random as ran
import math

p = ran.randint(0, 30)

print("The Computer Will choose a number between 0 and 30\ntry to Guess the number in less than 5 guesses")

for guesscompt in range(0, 5):
    nbrguessed = int(input("Guess the Number : "))

    if nbrguessed > p:
        print("Try Again! you guessed high")

    elif nbrguessed < p:
        print("Try Again! you guessed small")

    else:
        break

if nbrguessed == p:
    print("You made it! you guess right\nNumber of guesses is: " + str(guesscompt + 1))
else:
    print("You lose, The Chosen number is: " + str(p) + "\nNumber of guesses is: " + str(guesscompt + 1))
