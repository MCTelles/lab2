import random


def pullwords():
    words_file = open("wordsintxt.txt", "r")
    content = words_file.readlines()
    word = random.choice(content)
    print(word)
    return word


def pulltwoWords():
    words_file = open("wordsintxt.txt", "r")
    content = words_file.readlines()
    words_file.close()

    for index in range(1):
        firstword = random.choice(content).strip()
        secondword = random.choice(content).strip()

        while firstword == secondword:
            secondword = random.choice(content).strip()
    print(firstword, secondword)
    return firstword, secondword


def pullForWords(amount):
    with open("wordsintxt.txt", "r") as words_file:
        words = words_file.read().splitlines()
        if words:
            return random.sample(words, amount)
        else:
            return []
