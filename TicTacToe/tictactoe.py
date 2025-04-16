import random


class TicTacToe:

    @staticmethod
    def tictactoe():

        board_display = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        for row in board_display:
            print(" | ".join(str(cell) for cell in row))

        player1 = "x"
        player2 = "0"
        player = input("Lets start the game, What do you want X or 0?")

        if player == "x":
            print("you are player one, Computer will be player two")
            print("Make your move")
        elif player == "0":
            print("you are player two, Computer will be player one")
            print("computer will take move first")
        else:
            print("you have to choose btween X or 0")

        if player1 == "x":
            computer_choice = (random.randint(1, 9))
            for row in board_display:
                for i in range(len(row)):
                    if row[i] == computer_choice:
                        row[i] = "0"


TicTacToe.tictactoe()
