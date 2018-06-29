import os
import random
import sys

cells = [(x,y) for y in range(5) for x in range(5)]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def valid_moves(player):
    moves = ['LEFT', 'RIGHT', 'DOWN', 'UP']
    x, y = player
    if x == 4:
        moves.remove('RIGHT')
    if x == 0:
        moves.remove('LEFT')
    if y == 4:
        moves.remove('DOWN')
    if y == 0:
        moves.remove('UP')
    return moves

def move(player, moves):
    clear()
    grid(player)
    x, y = player
    print('You are currently in room ({},{})'.format(x,y))
    print('These are your valid moves: {}'.format(', '.join(moves)))
    while True:
        move = input('> ')
        move = move.upper()
        if move in moves:
            if move.lower() == 'left':
                x -= 1
            if move.lower() == 'right':
                x += 1
            if move.lower() == 'down':
                y += 1
            if move.lower() == 'up':
                y -= 1
            return x , y
        elif move.lower() == 'quit':
            sys.exit()
        else:
            print('That is not a direction, please enter a valid direction')
            continue

def grid(player):
    print(' _' *5)
    bottom = '_'
    marker = 'X'
    x , y = player
    for cell in cells:
        x1 , y1 = cell
        if x1 == 4:
            if x == x1 and y == y1:
                print('|{}|'.format(marker))
            else:
                print('|{}|'.format(bottom))
        else:
            if x == x1 and y == y1:
                print('|{}'.format(marker), end = '')
            else:
                print('|{}'.format(bottom), end = '')

def main(done):
    clear()
    input('Welcome to the dungeon game. Press enter to continue')
    player, door, monster = random.sample(cells, 3)

    while True:
        moves = valid_moves(player)
        player = move(player, moves)
        if player == door:
            print('You win!')
            done = True
        elif player == monster:
            print('You lose!')
            done = True

        if done:
            play_again = input('\nWould you like to play again? Y/n: ')
            if play_again.lower() != 'n':
                return main(done = False)
            else:
                print('Bye Bye')
                sys.exit()

done = False
main(done)
