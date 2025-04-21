import os


class WordScramble:
    def __init__(self):
        pass

    def reading_words(self):

        with open("easy_words.txt", "r") as file:
            easy = [word.strip() for word in file]
            for word in easy:
                print(word)

        with open("easy_words.txt", "r") as file:
            medium = [word.strip() for word in file]
            for word in medium:
                print(word)

        with open("hard_words.txt", "r") as file:
            hard = [word.strip() for word in file]
            for word in hard:
                print(word)


game = WordScramble()
game.reading_words()
