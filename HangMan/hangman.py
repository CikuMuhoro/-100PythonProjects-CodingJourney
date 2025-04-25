import random

word_list = [
    "apple", "banana", "orange", "guitar", "window", "pencil", "school", "python", "jungle", "laptop",
    "ocean", "flower", "secret", "shadow", "turtle", "camera", "desert", "island", "planet", "rocket",
    "bottle", "monkey", "button", "doctor", "market", "yellow", "garden", "coffee", "castle", "dragon",
    "frozen", "wizard", "thunder", "mirror", "puzzle", "cookie", "winter", "summer", "forest", "bridge",
    "helmet", "wallet", "circus", "cotton", "fabric", "tunnel", "credit", "stream", "dancer", "cloudy"
]

random_word = random.choice(word_list)
print(random_word)

hangman_art = {
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
