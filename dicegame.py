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
    
    while (playerChoice != 3):
        playerChoice = int(input("1: Start Game\n2: Rules\n3: Quit\n"))

        # Display rules to players
        if (playerChoice == 2):
            filePath = 'rules.txt'
            try:
                with open(filePath, 'r') as file:
                    fileContent = file.read()
                    print("\n" + fileContent + "\n")
            except FileNotFoundError:
                print("File not found :(")

        # Start game
        if (playerChoice == 1):
            continueGames = 0
            while (continueGames != 2):
                ref.resetGame(player1, player2)

                print("\n\nLet's begin!")

                round = 0
                while (ref.checkRoundWins(player1, player2) == 0):
                    round += 1
                    print("\n\ROUND " + str(round) + "\n")
                    
                    executeRound(player1, player2, ref)

                    if (ref.checkRoundWins(player1, player2) == 1 or ref.checkRoundWins(player1, player2) == 2):
                        print("\nFinal Score: ")
                        print(player1.name + ": " + str(player1.roundWins))
                        print(player2.name + ": " + str(player2.roundWins) + "\n")

                        continueGames = int(input("Play another game?\n1: Yes\n2: No\n"))

                        break

                    print("\nScore: ")
                    print(player1.name + ": " + str(player1.roundWins))
                    print(player2.name + ": " + str(player2.roundWins))

                    input("\nPress ENTER to continue")

# integration test (5)
# interactions between all classes
def executeRound(player1, player2, referee):
        referee.roundEnd = 0
        while referee.roundEnd != 1:
            player1.advantage = 0
            player2.advantage = 0

            # Determine who will have advantage this round
            print("Who will have the advantage...")
            print("Rolling die...\n")

            p1 = 0; p2 = 0
            while (p1 == p2):
                p1, p2 = referee.setPlayerAdvantage()
                
                # reroll if same
                if (p1 == p2):
                    continue

                print("Advantage die roll for " + player1.name + ": " + str(p1))
                print("Advantage die roll for " + player2.name + ": " + str(p2) + "\n")

                referee.determinePlayerAdvantage(player1, p1, player2, p2)

            if (player1.advantage == 1):
                print(player1.name + " has the advantage this round!\n")
            else:
                print(player2.name + " has the advantage this round!\n")

            # Players roll dice
            print("Rolling dice...\n")
            player1.rollDice()
            player2.rollDice()

            # Display results
            print(player1.name + "'s dice: [" + str(player1.die1) + "] " + "[" + str(player1.die2) + "]")
            print("Sum: " + str(sum(player1.dice)) + "\n")
            print(player2.name + "'s dice: [" + str(player2.die1) + "] " + "[" + str(player2.die2) + "]")
            print("Sum: " + str(sum(player2.dice)))

            # If there is a tie or zeroten, reroll
            if (referee.checkDice(player1, player2) == 1):
                print("\nRerolling dice...")
                input("\nPress ENTER to continue\n")
            else:
                referee.roundEnd = 1

if __name__ == "__main__":
    main()