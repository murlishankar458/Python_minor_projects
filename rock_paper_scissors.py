import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]
UserWins = 0
ComputerWins = 0

while True:
    
    UserInput = input("Choose Rock Paper scissors or q to quit-").lower()
    if UserInput == "q":
        quit()

    if UserInput not in options:
        continue #it goes to the starting of the while loop

    randomNumber = random.randint(0,2)
    # 0 For Rock 1 for paper and 2 for scissors
    computerpick = options[randomNumber]
    print("computer picked" , computerpick + ".") #if we add , it puts space but if we add + it does not put space


    if UserInput == computerpick:
        print("Tie!")

    elif UserInput == "rock" and computerpick == "scissors":
        print("You Win")
        UserWins += 1

    elif UserInput == "paper" and computerpick == "rock":
        print("You Win")
        UserWins += 1

    elif UserInput == "scissors" and computerpick == "paper":
        print("You Win")
        UserWins += 1

    else:
        print("Computer Wins")
        ComputerWins += 1

    if UserWins == 5:
        print("You won the game!")
        print("Your final score is", UserWins)
        print("Computer's final score is", ComputerWins)
        break

    elif ComputerWins == 5:
        print("Computer won the game!")
        print("Your final score is", UserWins)
        print("Computer's final score is", ComputerWins)
        break

    print("you won" , UserWins , "times." )
    print("compute wins" , ComputerWins , "times.")



