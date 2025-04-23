import os
import random


class WordScramble:

    def __init__(self):
        pass

    def easy_words(self):

        with open("easy_words.txt", "r") as file:
            easy = [word.strip() for word in file]
            for word in easy:
                return

    def medium_words(self):
        with open("medium_words.txt", "r") as file:
            medium = [word.strip() for word in file]
            for word in medium:
                return word

    def hard_words(self):
        with open("hard_words.txt", "r") as file:
            hard = [word.strip() for word in file]
            for word in hard:
                return

    def chose_level(self):
        level = input(
            "What level do you prefer easy,medium or hard?").lower()

        if level == "easy":
            self.level = "easy_words.txt"
            print("Easy level. You have up to five attemps for every word.")
        elif level == "medium":
            self.level = "medium_words.txt"
            print("Medium level. You have up to five attemps for every word.")
        elif level == "hard":
            self.level = "hard_words.txt"
            print("Hard level. You have up to five attemps for every word.")
        else:
            print("chose again among the three levels")

    def reading_words(self):
        # randomly pick a word from chosen list
        with open(self.level, "r") as file:
            words = [word.strip() for word in file]
            self.chosen_word = random.choice(words)

            # scramblering the chosen word
            chosen_word_list = list(self.chosen_word)
            random.shuffle(chosen_word_list)
            return ("".join(chosen_word_list))

    def playing_game(self):
        scrambled = self.reading_words()
        print("make a word from:", scrambled)

        attempt = 5

        while attempt > 0:
            guess = input("your geuse:").strip().lower()

            if guess == self.chosen_word.lower():
                print("correct!")
                return

            attempt -= 1

            if attempt == 0:

                print("Ooops! out of chances")

                print("The correct guess is:", self.chosen_word)
            else:
                print("try again!")


while True:

    game = WordScramble()
    game.chose_level()
    game.reading_words()
    game.playing_game()

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
