import random
import os
import sys

words = ['apple','orange','banana','strawberry','blueberry']

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end = ' ')
    else:
        print('_', end='')
    print('\n\n')
    for letter in secret_word:
        if letter in good_guesses:
            print(letter,end='')
        else:
            print('_', end='')
    print('')

def get_guesses(guesses):
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) != 1:
            print('You can only guess one letter')
        elif guess in guesses:
            print('You already guessed the letter')
        elif not guess.isalpha():
            print('You can only guess letters')
        else:
            return guess

def play(done):
    clear()
    secret_word = random.choice(words)
    bad_guesses = set()
    good_guesses = set()
    word_set = set(secret_word)

    while True:
        draw(bad_guesses,good_guesses,secret_word)
        guess = get_guesses(bad_guesses | good_guesses)

        if guess in word_set:
            good_guesses.add(guess)
            if not word_set^good_guesses:
                print('You win, the secret word was {}'.format(secret_word))
                done = True
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses,good_guesses,secret_word)
                print('You lost')
                done = True

        if done:
            play_again = input('Play again? Y/n').lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()

def welcome():
    start = input('Press enter/return to start or Q to quit ').lower()
    if start == 'q':
        print('Bye')
        sys.exit()
    else:
        return True # don't need this, but good practice to return a value fro a function

print('Welcome to letter guess game')
done = False
while True:
    clear()
    welcome()
    play(done)
