import random

def main():
    print('Pick a number between 1 - 100. I will guess the number')
    guess_remaining = 8
    start = 1
    end = 100
    while guess_remaining > 0:
        guess = random.randint(start,end)
        reply = input('Is your number {}? '.format(guess))
        if reply.lower() == 'y':
            print('I knew I could get it!')
            break
        elif reply.lower() == 'n':
            hl = input('Is your number higher (h) or lower (l)? ')
            if hl == 'h':
                start = guess + 1
            elif hl == 'l':
                end = guess - 1
        guess_remaining -= 1

main()
while True:
    ans = input('\nWould you like to play again? (y/n) \n')
    if ans.lower() == 'y':
        main()
    else:
        print('Thanks for playing')
        break
