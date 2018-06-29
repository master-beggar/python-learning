import sys
import os

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_item(shopping_list):
    while True:
        item = input('> ').lower()
        if item in shopping_list:
            print('You already have this item in list')
            continue
        elif item is '':
            continue
        else:
            return shopping_list.append(item)

def display(shopping_list):
    print('These are the items in your list: ')
    print('\n')
    for num, item in enumerate(shopping_list,1):
        print('{}. {}'.format(num, item))
    print('\n')

shopping_list = []
while True: 
    clearscreen()
    display(shopping_list)
    add_item(shopping_list)
