import random

word_list = ['dog','dragon','orange']
list_length = int(len(word_list))

the_word = word_list[random.randint(0,list_length-1)]
hidden = list('-'*len(the_word))

trys = 5
while trys > 0:
    letter = input('Pick a letter that is in the word: ')
    if letter.lower() in the_word:
        hidden[the_word.index(letter)] = letter.lower()
    else:
        print('Try again')
        trys -= 1
    if ''.join(hidden) == the_word:
        print('You got it!')
        break
    print(''.join(hidden))
