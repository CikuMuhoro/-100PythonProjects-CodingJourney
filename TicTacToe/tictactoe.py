class TicTacToe:

    @staticmethod
    def tictactoe():

        board_display = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]
        for row in board_display:
            print(" | ".join(str(cell) for cell in row))


TicTacToe.tictactoe()
