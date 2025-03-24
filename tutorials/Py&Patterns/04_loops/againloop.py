while True:
    while True:
        word = input("Enter the magic word: ")
        if word == "please":
            print("this is correct, you win!")
            break
        else:
            print("this is not correct, try again!")
    word = input("Type 'again' to play again: ")
    if word != "again":
        break
print("Thank you for playing this game")

