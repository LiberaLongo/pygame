magicNumber = 3
while True:
    word = input("What is the magic number? ")
    try:
        playerNumber = int(word)
    except ValueError:
        print("Please type a integer number without decimals!")
        continue
    if playerNumber == magicNumber:
        print("This is correct! You win!")
        break
    print("This is not the magic number. Try Again!")
