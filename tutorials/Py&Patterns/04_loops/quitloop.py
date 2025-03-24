repeat = True
while repeat:
    while True:
        word = input("Enter the magic word: ")
        if word == "please":
            print("this is correct, you win!")
            break
        elif word == "quit":
            repeat = False
            break
        else:
            print("this is not correct, try again!")
print("Thank you for playing this game")

