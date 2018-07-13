import pandas as pd
import csv

url = 'https://www.fastenal.com/products/details/'

part_numbers = []

with open('fastenal_hardware.txt') as file:
    for line in file:
        line = line.strip()
        part_numbers.append(line)

pn_df = pd.DataFrame(columns=['Part Number','Type', 'Diameter', 'Length', 'Material', 'Finish'])

count = 1

for pn in part_numbers:
    try:
        df = pd.read_html(url + pn, attrs = {'class':'table product__attribute--info'}, index_col = 0)[0]
        try:
            typ, length, material, finish = (df.loc['Type'].values[0], df.loc['Length'].values[0], df.loc['Material'].values[0], df.loc['Finish'].values[0])
            if 'Diameter - Thread Size' in df.index:
                diameter = df.loc['Diameter - Thread Size'].values[0]
            elif 'Dia/Thread Size' in df.index:
                diameter = df.loc['Dia/Thread Size'].values[0]
            else:
                diameter = df.loc['Diameter-Thread Size'].values[0]
            print('{} | {} | {} | {} | {} | {}'.format(pn, typ, diameter, length, material, finish))
            pn_df.loc[len(pn_df)] = (pn, typ, diameter, length, material, finish)
        except:
            typ, material, finish = (df.loc['Type'].values[0], df.loc['Material'].values[0], df.loc['Finish'].values[0])
            try:
                diameter = df.loc['Nominal Size'].values[0]
            except:
                try:
                    diameter = df.loc['Bolt Size'].values[0]
                except:
                    try:
                        diameter = df.loc['Diameter-Thread Size'].values[0]
                    except:
                        try:
                            diameter = df.loc['Dia/Thread Size'].values[0]
                        except:
                            diameter = df.loc['Diameter'].values[0]
            try:
                length = df.loc['Length'].values[0]
                print('{} | {} | {} | {} | {} \ {}'.format(pn, typ, diameter, length, material, finish))
                pn_df.loc[len(pn_df)] = (pn, typ, diameter, length, material, finish)
            except:
                print('{} | {} | {} | N/A | {} | {}'.format(pn, typ, diameter, material, finish))
                pn_df.loc[len(pn_df)] = (pn, typ, diameter, '-', material, finish)
    except:
        continue
    
#  for testing purposes only; only outputs first three rows to csv file:
##    count += 1
##    if count > 10:
##        break

pn_df.to_csv('fastenal-hardware.csv', index=False, quoting=csv.QUOTE_NONE)
#, quoting=csv.QUOTE_NONE
