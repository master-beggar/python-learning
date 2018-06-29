import os

def clear_screen():
    os.system("cls" if os.name == 'nt' else 'clear')

def instructions():
    clear_screen()
    print('Enter items that you want to add to your list')
    print('Once you are done, type "DONE" to exit and view your shopping list')

def show_list():
    clear_screen()
    print('These are {} items in your shopping list: '.format(len(shopping_list)))
    for c,i in enumerate(shopping_list,1):
        print(str(c) + '. ' + i)
    print('-'*10)

def deletion():
    item_to_delete = input('Type out the name of the item you want to remove from the list: ')
    shopping_list.remove(item_to_delete)

def add_new():
    if len(shopping_list):
        position = input('Where should I add {}?\n'.format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1,new_item)
    else:
        shopping_list.append(new_item)
    show_list()

instructions()

shopping_list = []

def main():
    while True:
        new_item = input('> ')
        if new_item.lower() == 'done':
            break
        elif new_item.lower() == 'help':
            instructions()
            continue
        elif new_item.lower() == 'show':
            show_list()
            continue
        elif new_item.lower() == 'del':
            deletion()
            show_list()
            continue
        else:
            add_new()
main()
