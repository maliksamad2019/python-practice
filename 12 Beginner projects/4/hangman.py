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
    used_alphabets = set()

    lives = 6    

    while lives > 0 and len(word_letters) > 0: 
        print('you have used: ', ' '.join(used_alphabets))
        words_list = [letter if letter in used_alphabets else '-' for letter in word]

        print(' '.join(words_list))
        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabets - used_alphabets :
            used_alphabets.add(user_letter)
            if user_letter in word_letters  :
                word_letters.remove(user_letter)
                print('your guess is correct!')
            else:
                lives-=1
                print('try again!')
        elif user_letter in used_alphabets:
            print('character already used!')
        else:
            print('invalid character!')
    if len(word_letters) == 0:
        print(f'you have guessed the word correctly! its {word}')
    else:
        print(f'you have failed to guessed the word! its {word}')





# print(get_valid_word())
hangman()


