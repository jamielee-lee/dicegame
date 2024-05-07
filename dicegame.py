# Jamie Lee
# CS 333
# Final Project
# Dice Game

from player import Player
from referee import Referee

def main():
    print("\n\n----------------------------\n")
    print("DICE GAME\n")
    print("----------------------------\n\n")

    name1 = input("Player 1, what is your name?\n")
    player1 = Player(name1)

    name2 = input("Player 2, what is your name?\n")
    player2 = Player(name2)

    print("\nWelcome to the table! :)\n")
    ref = Referee()

    playerChoice = 0
    
    while (playerChoice != 1 | playerChoice != 3):
        playerChoice = int(input("1: Start Game\n2: Rules\n3: Quit\n"))

        if (playerChoice == 2):
            filePath = 'rules.txt'
            try:
                with open(filePath, 'r') as file:
                    fileContent = file.read()
                    print(fileContent)
            except FileNotFoundError:
                print("File not found :(")

    if (playerChoice == 1):
        print("\n\nLet's begin!")

        round = 0
        while (ref.checkRoundWins(player1, player2) != 1):
            round += 1
            print("\n\nRound " + str(round) + "\n")
            
            executeRound(player1, player2, ref)

            if (ref.checkRoundWins(player1, player2) == 1):
                break

            print(player1.name + "'s wins: " + str(player1.roundWins))
            print(player2.name + "'s wins: " + str(player2.roundWins))

            input("\nPress ENTER to continue")

def executeRound(player1, player2, referee):
        referee.roundEnd = 0
        while referee.roundEnd != 1:
            # Players roll dice
            print("Rolling dice...")
            player1.rollDice()
            player2.rollDice()

            # Display results
            print(player1.name + "'s dice: [" + str(player1.die1) + "] " + "[" + str(player1.die2) + "]")
            print("Sum: " + str(sum(player1.dice)) + "\n")
            print(player2.name + "'s dice: [" + str(player2.die1) + "] " + "[" + str(player2.die2) + "]")
            print("Sum: " + str(sum(player2.dice)))

            if (referee.checkDice(player1, player2) == 1):
                print("\nRerolling dice...")
                input("\nPress ENTER to continue\n")
            else:
                referee.roundEnd = 1

if __name__ == "__main__":
    main()