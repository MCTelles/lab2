import random


def pullwords():
    words_file = open("wordsintxt.txt", "r")
    content = words_file.readlines()
    word = random.choice(content)

    print(word)
    return word
