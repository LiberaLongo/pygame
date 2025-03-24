while True:
    word = input("Enter the magic word: ")
    if word != "please":
        print("this is not correct, you lost :-(")
        continue
    print("this is correct, you win!")
    break
print("Thank you for playing this game")

