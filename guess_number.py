import random

#You Have 7 Guesses For This Game

range_of_number = input("Type a number: ")

if range_of_number.isdigit():
    range_of_number = int(range_of_number)

    if range_of_number <= 0:
        print("Type a Number Greater Than Zero")
        quit()
else:
    print("Please type a number next time")
    quit()

randomNumber = random.randint(0, range_of_number)

guesses = 0
max_guesses = 7

while True:

    userGuess = input("\nGuess the number: ")

    if userGuess.isdigit():
        userGuess = int(userGuess)
        guesses += 1
    else:
        print("Please type a number next time")
        continue

    if userGuess == randomNumber:
        print("You Got it Right!")
        print("You guessed it in", guesses, "attempts.")
        break

    elif userGuess > randomNumber:
        print("You are above the number")
    else:
        print("You are below the number")

    if guesses >= max_guesses:
        print("\nGame Over!")
        print("You used all 7 guesses.")
        print("The number was", randomNumber)
        break