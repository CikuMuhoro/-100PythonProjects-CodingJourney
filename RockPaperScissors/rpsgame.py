import random


class RockPaperScissors:
    @staticmethod
    def rpsgame():
        allchoices = ["rock", "paper", "scissors"]

        player_pick = input("shoot between rock paper and scissors: ").lower()
        computer_pick = random.choice(allchoices)
        print(f"computer choice is: {computer_pick}")

        if player_pick == computer_pick:
            print("its a tie!")
        elif (computer_pick == "rock" and player_pick == "scissors") or \
             (computer_pick == "scissors" and player_pick == "paper") or \
             (computer_pick == "paper" and player_pick == "rock"):
            print("Computer won!!")

        else:
            print("You win!!")


RockPaperScissors.rpsgame()
