print('This is a shopping list application')

def instructions():
    print('Enter items that you want to add to your list')
    print('Once you are done, type "DONE" to exit and view your shopping list')

def shopping_show():
    print('These are {} items in your shopping list: '.format(len(shopping_list)))
    for item in shopping_list:
        print(item)

def deletion():
    item_to_delete = input('Type out the name of the item you want to remove from the list: ')
    shopping_list.remove(item_to_delete)

instructions()

shopping_list = []

def main():
    while True:
        item = input('> ')
        if item.lower() == 'done':
            break
        elif item.lower() == 'help':
            instructions()
            continue
        elif item.lower() == 'show':
            shopping_show()
            continue
        elif item.lower() == 'del':
            deletion()
            continue
        shopping_list.append(item)

    shopping_show()

main()
