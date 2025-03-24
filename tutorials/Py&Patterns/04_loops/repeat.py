repeat = True
while repeat:
    word = input("Enter the magic word: ")
    if word == "please":
        print("this is correct, you win!")
        repeat = False
    else:
        print("this is not correct, you lost :-(")
print("Thank you for playing this game")

