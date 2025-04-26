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
        # print(self.random_word)

    def hangman_art(self):
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

    def hangman_loop(sef):


game = Hangman()
game.hangman_words()
