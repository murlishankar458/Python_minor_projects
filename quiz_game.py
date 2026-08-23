print("Welcome To The Quiz Game")

playing= input("Do You Want To Play (yes/No)? " )

if playing.lower() == "no":
    quit()

elif playing.lower() == "yes":
    print("Let's Play")

else:
    print("Invalid Answer")
    quit()

while True:

    score = 0



    # QUESTION 1
    print("Which keyword is used to define a function in Python? ")
    print("A. function")
    print("B. def")
    print("C. fun")
    print("D. define")

    answer = input ("Your Answer : ")


    if answer.lower()== "b":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )

    # QUESTION 2

    print("Which data type is used to store multiple values in an ordered collection? ")
    print("A. list")
    print("B. int")
    print("C. bool")
    print("D. float")

    answer = input ("Your Answer : ")


    if answer.lower()== "a":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )


    # QUESTION 3

    print("What is the output of print(2 + 3)? ")
    print("A. 23")
    print("B. 5")
    print("C. 6")
    print("D. 2+3")

    answer = input ("Your Answer : ")


    if answer.lower()== "b":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )


    # QUESTION 4

    print("Which symbol is used for a comment in Python? ")
    print("A. //")
    print("B. /*")
    print("C. #")
    print("D. --")

    answer = input ("Your Answer : ")


    if answer.lower()== "c":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )


    # QUESTION 5


    print("Which function is used to get input from the user? ")
    print("A. get()")
    print("B. input()")
    print("C. read()")
    print("D. scan()")

    answer = input ("Your Answer : ")


    if answer.lower()== "b":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )

    # QUESTION 6


    print("Which of these is a Python dictionary?")
    print("A. [1, 2, 3]")
    print("B. (1, 2, 3)")
    print('C. {"name": "John"}')
    print("D. {1, 2, 3}")

    answer = input ("Your Answer : ")


    if answer.lower()== "c":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )

    # QUESTION 7

    print("What does len() do?")
    print("A. Converts a value to integer")
    print("B. Returns the number of items/characters")
    print("C. Deletes a value")
    print("D. Sorts a list")

    answer = input ("Your Answer : ")


    if answer.lower()== "b":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )

    # QUESTION 8
    print("Which loop is commonly used to iterate through a sequence?")
    print("A. repeat")
    print("B. loop")
    print("C. for")
    print("D. iterate")

    answer = input ("Your Answer : ")


    if answer.lower()== "c":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )

    # QUESTION 9
    print("What is the result of 10 // 3?")
    print("A. 3")
    print("B. 3.33")
    print("C. 1")
    print("D. 4")

    answer = input ("Your Answer : ")


    if answer.lower()== "a":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )

    # QUESTION 10
    print("Which keyword is used when you want to stop a loop immediately?")
    print("A. stop")
    print("B. exit")
    print("C. break")
    print("D. end")

    answer = input ("Your Answer : ")


    if answer.lower()== "c":
        print("Correct, Great")
        score += 1

    else:
        print("Incorrect")

    print("Your score is ",score )

    perct = score/10 *100
    print("\n your percentage is  ", perct,"%")

    again = input("Do you want to play again? (yes/no): ")

    if again.lower() == "no":
        break