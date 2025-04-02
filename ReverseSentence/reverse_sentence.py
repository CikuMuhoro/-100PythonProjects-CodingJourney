def resverse_sentence():
    sentence = input("Enter your sentence: ")
    words = sentence.split()
    word_count = len(words)
    if word_count < 2:
        print("Enter a sentence")
    else:
        reversed_sentence = " ".join(sentence.split()[::-1])
        print(reversed_sentence)


resverse_sentence()
