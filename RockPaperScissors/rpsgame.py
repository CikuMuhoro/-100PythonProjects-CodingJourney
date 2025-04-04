import random


class RockPaperScissors:
    @staticmethod
    def rpsgame():
        allchoices = ["rock", "paper", "scissors"]

        player_pick = input("shoot between rock paper and scissors:")
        computer_pick = random.choice(allchoices)
        print(f"computer choise is: {computer_pick}")


RockPaperScissors.rpsgame()
