# python hangman.py
from words import words
import random
import string

def get_valid_word():
    word = random.choice(words)
    while '_' in word or ' 'in word:
        word= random.choice(word)

    return word.upper()

def hangman():
    word = get_valid_word()
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    print(alphabets, word_letters,word)

# print(get_valid_word())
hangman()


