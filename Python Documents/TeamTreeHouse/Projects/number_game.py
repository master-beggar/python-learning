import random

# generate a random number between 1 and 10
def main():
    the_number = random.randint(1,10)
    guess_remaining = 5
    while guess_remaining > 0:
        try:
            guess = int(input('Guess the number: '))
        except ValueError:
            print('{} is not a number'.format(guess))
            continue
        else:
            if guess == the_number:
                print('You got the number!')
                break
            elif guess > the_number:
                print('Too high')
            elif guess < the_number:
                print('Too low')
        guess_remaining -= 1

main()
while True:
    ans = input('\nWould you like to play again? (y/n) \n')
    if ans.lower() == 'y':
        main()
    else:
        print('Thanks for playing')
        break
