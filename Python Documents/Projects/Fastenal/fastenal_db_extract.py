import sqlite3
import random

conn = sqlite3.connect('Fastenal.sqlite')
cur = conn.cursor()

def make_dic():
    db = cur.fetchall()
    name = {}
    for type in db:
        name[type[1]] = type[0]
    return name

def get_input(the_dic):
    while True:
        type_input = input('\nPick the number: ')
        if len(type_input) < 1:
            print('Please enter a number')
            continue
        elif type_input.isalpha():
            print('You entered a letter, please enter a number')
            continue
        elif int(type_input) not in the_dic.keys():
            print('You did not enter a right number')
        else:
            type_input = int(type_input)
            return type_input

cur.execute('''
SELECT Types.type, Types.id
FROM Types
ORDER BY Types.type
''')
types = make_dic()

print('Theres are the different types: \n')
for k,v in types.items():
    print(str(k) +'. ' + v)

type_input = get_input(types)

cur.execute('''
SELECT Diameter.diameter, Diameter.id
FROM Diameter JOIN Types JOIN Part_Number
ON Part_Number.type = Types.id and Part_Number.diameter = Diameter.id and Types.id = ?
ORDER BY Diameter.diameter
''', (type_input,))

diameters = make_dic()

print('Theres are the different sizes: \n')
for k,v in diameters.items():
    print(str(k) +'. ' + v)

diam_input = get_input(diameters)

cur.execute('''
SELECT Part_Number.length, Part_Number.pn_id
FROM Part_Number JOIN Types JOIN Diameter
ON Part_Number.type = Types.id and Part_Number.diameter = Diameter.id
WHERE Types.id = ? and Diameter.id = ?
''', (type_input, diam_input))

lengths = make_dic()

print('Theres are the different lengths: \n')
for k,v in lengths.items():
    print(str(k) +'. ' + v)

len_input = get_input(lengths)

cur.execute('''
SELECT Part_Number.pn
FROM Part_Number JOIN Types JOIN Diameter
ON Part_Number.type = Types.id and Part_Number.diameter = Diameter.id
WHERE Types.id = ? and Diameter.id = ? and Part_Number.pn_id = ?
''', (type_input, diam_input, len_input))


item = cur.fetchall()
print(item[0][0])
