import random


class TicTacToe:

    def __init__(self):

        self.board_display = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.player = None
        self.computer = None

    def show_board(self):
        for row in self.board_display:
            print(" | ".join(str(cell) for cell in row))
            print()

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

    def player_moves(self):

        while True:
            try:

                move = int(
                    input("choose a position(1-9) should not be taken:"))
                if move < 1 or move > 9:
                    print("make a valid choice")
                    continue

                placed = False

                for i in range(3):
                    for j in range(3):
                        if self.board_display[i][j] == move:
                            self.board_display[i][j] = self.player
                            self.show_board()
                            placed = True
                            return

                if not placed:
                    print("spot already taken")

            except ValueError:
                print("please enter a valid number")

    def computer_moves(self):
        available = []
        for i in range(3):
            for j in range(3):
                if isinstance(self.board_display[i][j], int):
                    available.append((i, j))

        if available:
            i, j = random.choice(available)
            self.board_display[i][j] = self.computer
            print("Computer chose a move:")
            self.show_board()

    def chek_winner(self, symbol):
        # check row and columns for the winner
        for i in range(3):
            if all(self.board_display[i][j] == symbol for j in range(3)) or \
               all(self.board_display[j][i] == symbol for j in range(3)):
                return True

            # Check both diagonals for the winner
        if all(self.board_display[i][i] == symbol for i in range(3)) or \
           all(self.board_display[i][2 - i] == symbol for i in range(3)):
            return True

        return False

    def draw(self):
        return all(not isinstance(cell, int) for row in self.board_display for cell in row)


game = TicTacToe()
game.show_board()
game.player_symbol()

if game.player:
    while True:
        game.player_moves()
        if game.chek_winner(game.player):
            print("you win!")
            break
        if game.draw():
            print("its a draw!")
            break

        game.computer_moves()
        if game.chek_winner(game.computer):
            print("Computer wins!")
            break
        if game.draw():
            print("its a draw!")
            break
