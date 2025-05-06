import random
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
        self.guess_word = ["_" for _ in self.random_word]
        self.guessed_letters = set()
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

            4: ("O",
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
        mistakes = 6 - self.lives  # number of incorrect guesses made
        head, body, legs = self.hangman_art[mistakes]
        print(" ____")  # top of gallows
        print(" |  |")  # vertical support line
        print(f" | {head}")  # head line
        print(f" | {body}")  # body adn arms
        print(f" | {legs}")  # legs line
        print(" |")  # base of stand
        print("_|_")  # floor line

    def display_game_state(self):
        """ Print the current word and guessed letters. """
        print("\nCurrent word:", " ".join(self.guess_word))
        print(f"Guessed so far: {', '.join(sorted(self.guessed_letters))}")

    def hangman_loop(self):

        # self.guess_word = ["_" for _ in self.random_word]
        # a
        # self.guessed_letter = set()

        while self.lives > 0 and "_" in self.guess_word:
            clear_screen()
            self.print_hangman()
            self.display_game_state()
            guess = input("Guess a letter: "). lower()

        # guess = input("Guess correctly to save Hangman:" + "".join(self.guess_word)).lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single valid letter.")
                continue

            if guess in self.guessed_letters:
                print("You already guessed that letter.")
                continue

            self.guessed_letters.add(guess)

            if guess in self.random_word:
                print("Great guess!")
                for i, letter in enumerate(self.random_word):
                    if letter == guess:
                        self.guess_word[i] = guess

            else:
                self.lives -= 1
                print("ooh no!", self.lives)
                # self.print_hangman()
                # print("Current word:", "  ".join(self.guess_word))

        # Game over condition
        if "_" not in self.guess_word:
            print(f"You saved hangman! The word was: {self.random_word}")
        else:
            print(f"Game over! The word was: {self.random_word}")


while True:
    game = Hangman()
    game.hangman_words()
    game.hangman_art_image()
    game.hangman_loop()

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
