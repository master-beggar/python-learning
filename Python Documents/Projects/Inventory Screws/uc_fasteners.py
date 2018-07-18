import pandas as pd
##import csv

url = 'https://www.uccomponents.com/cds_catalog_product.php?id='

part_numbers = []

with open('uc-fasteners.txt') as file:
    for line in file:
        line = line.strip()
        part_numbers.append(line)

pn_df = pd.DataFrame(columns=['Part Number','Size', 'Length', 'Type', 'Material', 'Unit System'])

##count = 1

for pn in part_numbers:
    try:
        df = pd.read_html(url + pn, attrs = {'class':'cds-attribute-table'}, index_col = 0)[0]
        try:
            desc, size, length, material, unit = (df.loc['Description'].values[0], df.loc['Thread Size Nom.'].values[0], df.loc['Length'].values[0], df.loc['Material'].values[0], df.loc['Unit System'].values[0])
            print('{} | {} | {} | {} | {}'.format(pn, size, length, desc, material))
            pn_df.loc[len(pn_df)] = (pn, size, length, desc, material, unit)
        except:
            desc, size, material, unit = (df.loc['Description'].values[0], df.loc['Thread Size Nom.'].values[0], df.loc['Material'].values[0], df.loc['Unit System'].values[0])
            print('{} | {} | {} | {}'.format(pn, size, desc, material))
            pn_df.loc[len(pn_df)] = (pn, size, '-', desc, material, unit)
    except:
        continue
    
##  for testing purposes only; only outputs first three rows to csv file:
##    count += 1
##    if count > 3:
##        break

pn_df.to_csv('uc-fasteners.csv', index=False)
#, quoting=csv.QUOTE_NONE
