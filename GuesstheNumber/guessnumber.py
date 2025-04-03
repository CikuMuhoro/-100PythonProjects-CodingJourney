import random


class guessnumber:
    @staticmethod
    def guess_game():
        while True:
            try:
                myguess = random.randint(1, 100)

                guess = int(input("Guess a number:"))

                if myguess == guess:
                    print("Great geuss, This it.")
                    break

                elif abs(myguess - guess) <= 5:
                    print("You are almost ther, take another guess")

                else:
                    print(("not any close"))
                    print(f"my guess wa {myguess}")

            except ValueError:
                print("It has to be an integer between 1 and 100")


guessnumber.guess_game()
