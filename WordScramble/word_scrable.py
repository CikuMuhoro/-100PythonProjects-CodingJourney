import os


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
        level = input("What level do you prefer easy,medium or hard?").lower()

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


game = WordScramble()
game.reading_words()
game.chose_level()
