import random


class Hangman:
    def hangman_words(self):
        self.word_list = [
            "apple", "banana", "orange", "guitar", "window", "pencil", "school", "python", "jungle", "laptop",
            "ocean", "flower", "secret", "shadow", "turtle", "camera", "desert", "island", "planet", "rocket",
            "bottle", "monkey", "button", "doctor", "market", "yellow", "garden", "coffee", "castle", "dragon",
            "frozen", "wizard", "thunder", "mirror", "puzzle", "cookie", "winter", "summer", "forest", "bridge",
            "helmet", "wallet", "circus", "cotton", "fabric", "tunnel", "credit", "stream", "dancer", "cloudy"
        ]

        self.random_word = random.choice(self.word_list)
        self.lives = 6
        # print(self.random_word)

    def hangman_art_image(self):
        self.hangman_art = {
            0: ("",
                "",
                ""),

            1: ("O",
                "",
                ""),

            2: ("O",
                "|",
                ""),

            3: ("O",
                "/|",
                ""),

            4: ("0",
                "/|\\",
                ""),

            5: ("O",
                "/|\\",
                "/"),

            6: ("O",
                "/|\\",
                "/\\"),

        }

    def print_hangman(self):
        head, body, legs = self.hangman_art[self.lives]
        print(" ____")  # top of gallows
        print(" |  |")  # vertical support line
        print(f" | {head}")  # haed line
        print(f" | {body}")  # body adn arms
        print(f" | {legs}")  # legs line
        print("  |")  # base of stand
        print("__|__")  # floor line

    def hangman_loop(self):
        self.guess_word = [" _" for _ in self.random_word]

        guess = input("Guess correctly to save Hangman:" +
                      "".join(self.guess_word)).lower()

        if guess in self.guess_word:
            for i, letter in enumerate(self.guess_word):
                if letter == guess:
                    self.guess_word[i] = guess
                    print("greatGuess!")

                else:
                    self.lives -= 1
                    print("ooh no!", self.lives)
                    self.print_hangman()
                print("Current word:", "  ".join(self.display_word))


game = Hangman()
game.hangman_words()
game.hangman_art_image()
game.hangman_loop()
