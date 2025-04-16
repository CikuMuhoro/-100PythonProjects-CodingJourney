import random


class TicTacToe:

    def show_board(self):

        self.board_display = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.player = None
        self.computer = None

        for row in self.board_display:
            print(" | ".join(str(cell) for cell in row))

    def player_symbol(self):
        player = input("Lets start the game, What do you want X or 0?").lower()
        if player == "x":
            self.player = "x"
            self.computer = "0"
            print("computer will be player 0")
        elif player == "0":
            self.player = "0"
            self.computer = "x"
            print("computer will be player X")
        else:
            print("invalid choise")
            self.player = None
            self.computer = None

    # def positioning_moves(self):


game = TicTacToe()
game.show_board()
game.player_symbol()
