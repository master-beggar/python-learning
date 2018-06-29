import random
import os 

word_list = (
    'apples',
    'bananas',
    'carrots',
    'spinach',
    'brocoli'
    )

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw(good_guesses, bad_guesses, secret_word):
    clear()
    print('Strikes: {}/7'.format(str(len(bad_guesses))))
    print('\n')
    print('Bad Guesses: ', end='')
    for letter in bad_guesses:
        print(letter, end =' ')
    print('\n')
    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end = '')
        else:
            print('_', end = ' ')
    print('\n')
    print('-' *20)

def get_guess(guesses, good_guesses, bad_guesses, secret_word):
    while True:
        draw(good_guesses, bad_guesses, secret_word)
        guess = input('> ').lower()
        if len(guess) != 1:
            input('You can only guess a letter')
            continue
        elif not guess.isalpha():
            input('{} is not a letter. You can only guess a letter'.format(guess))
            continue
        elif guess.lower() in guesses:
            input('You have already guessed {}'.format(guess))
        else:
            return guess
                    
def playing(done):
    secret_word = random.choice(word_list)
    bad_guesses = set()
    good_guesses = set()
    the_word = set(secret_word)

    while done:
        guess = get_guess(bad_guesses|good_guesses, good_guesses, bad_guesses, secret_word)
        if guess in secret_word:
            good_guesses.add(guess)
            if not the_word^good_guesses:
                print('You win. The secret word was {}'.format(secret_word))
                done = False
                break
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == 7:
                print('You lose. The secret word was {}'.format(secret_word))
                done = False
                break

    if not done:
        play_again = input('Do you want to play again? Y/n')
        if play_again.lower() != 'n':
            return playing(done = True)
        else:
            print('Come again')
    
done = True
playing(done)
    
