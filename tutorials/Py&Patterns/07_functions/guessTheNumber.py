import random
def askPlayer():
    while True:
        word = input("What is the magic number? ")
        if word == "quit":
            return None

        try:
            playerNumber = int(word)
            break
        except ValueError:
            print("Please type an integer number without decimals!")
            continue
    return playerNumber
       
def runGame():
    magicNumber = random.randint(1,10)
    guessCount = 0
    while True:
        playerNumber = askPlayer()
        if playerNumber is None:
            break
        guessCount += 1

        if playerNumber == magicNumber:
            print("This is correct! You win!")
            print("You guessed the magic number in {} guesses.".format(guessCount))
            break
        elif magicNumber < playerNumber:
            print("The magic number is lower")
        elif magicNumber > playerNumber:
            print("The magic number is higher")

        #print("This is not the magic number. Try Again!")

while True:
    print("Game menu")
    print("1) start a new game")
    print("2) quit")
    choice = input("Enter yout choice: ")
    if choice == "1":
        runGame()
    elif choice == "2":
        break
