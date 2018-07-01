import sqlite3
import pandas as pd
import csv

conn = sqlite3.connect('Fastenal.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Types;
DROP TABLE IF EXISTS Diameter;
DROP TABLE IF EXISTS Part_Number;

CREATE TABLE Types (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    type   TEXT UNIQUE
);

CREATE TABLE Diameter (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    diameter  TEXT UNIQUE
);

CREATE TABLE Part_Number (
    pn_id       INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT UNIQUE,
    pn          TEXT UNIQUE,
    length      TEXT,
    type        TEXT,
    diameter    TEXT
)
''')

with open('Fasteners.txt') as file:
    pn_list = []
    for line in file:
        line = line.strip()
        line = line.split('\t')
        if len(line) > 1:
            pn_list.append(line[0])

new_table = pd.DataFrame(columns=['Part Number','Type', 'Diameter', 'Length'])

count = 0

for pn in pn_list:
    search_url = 'https://www.fastenal.com/products/details/' + pn
    table = pd.read_html(search_url, index_col = 0, attrs={'class':'table product__attribute--info'})[0]

    if 'Type' in table.index and 'Length' in table.index:
        if any(table.loc['Type'].str.contains('Screw')):
            try:
                type = table.loc['Type'].values[0]
                length = table.loc['Length'].values[0]
                if 'Diameter - Thread Size' in table.index:
                    diameter = table.loc['Diameter - Thread Size'].values[0]
                elif 'Dia/Thread Size' in table.index:
                    diameter = table.loc['Dia/Thread Size'].values[0]
                else:
                    diameter = table.loc['Diameter-Thread Size'].values[0]
            except:
                continue
            else:
                cur.execute('''INSERT OR IGNORE INTO Types (type)
                    VALUES ( ? )''', ( type, ) )
                cur.execute('SELECT id FROM Types WHERE type = ? ', (type, ))
                type_id = cur.fetchone()[0]

                cur.execute('''INSERT OR IGNORE INTO Diameter (diameter)
                    VALUES ( ? )''', ( diameter, ) )
                cur.execute('SELECT id FROM Diameter WHERE diameter = ? ', (diameter, ))
                diameter_id = cur.fetchone()[0]

                cur.execute('''INSERT OR REPLACE INTO Part_Number
                    (pn, type, diameter, length)
                    VALUES ( ?, ?, ?, ? )''',
                    ( pn, type_id, diameter_id, length ) )

                conn.commit()

                new_table.loc[len(new_table)] = (pn, type, diameter, length)

    # if any(table.index.str.contains('Diameter -')):
    #     print(table.loc['Diameter - Thread Size'])
    # if table.loc['Type'].str.contains('Fender').bool:
    #     print(table.loc['Type'].str.contains('Fender'))
    #     print(table.loc['System of Measurement'])

new_table.to_csv('fasteners.csv', index=False, quoting=csv.QUOTE_NONE)
