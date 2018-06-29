# get dictionary of unique values in TYPE column
# make selection of type in TYPE column; and return value
# get dictionary of unique values in some column subset by the previous return

import pandas as pd

try:
    table = pd.read_excel(r'C:\Users\Ahmad Walid Naimi\Desktop\Python Documents\Projects\AFR (add fastener request).xlsx')
except:
    table = pd.read_excel(r'W:\Engineering\Mechanical\AFR (add fastener request).xlsx')

table_new = table.drop(columns=['Unnamed: 0', 'Inventory #\nOld', 'Inventory #\nNew', 'type2', 'size2', 'feature', 'thread', 'length2', 'THEORETICAL\nINV PART #'])
table_new.fillna('', inplace=True)
table_new.drop(table[table['PART NUMBER']==''].index, inplace=True)
table_new.LENGTH = table_new.LENGTH.astype(str)

# function that makes dictionaries of unique values in selected column and enumerates them
def make_dic(data):
    name = dict()
    for k,v in enumerate(sorted(set(filter(None,list(data)))),start=1):
        name[k] = v
    return name

def make_selection(q1, q2, data):
    print(q1)
    for k,v in data.items():
        print(str(k)+'.', v)
    print('\n')
    data_input = input(q2)
    data_num = int(data_input)
    data_select = data[data_num]
    return data_select

def make_subset(data, subsetter):
    name = dict()
    for k,v in enumerate(sorted(set(list(data[subsetter]))),start=1):
        name[k] = v
    return name

type_df = make_dic(table_new.TYPE)
type_select = make_selection('These are the types of screws: ', 'Which type of screw? Enter the number: ', type_df)
size_subset = make_subset(table_new.SIZE, table_new.TYPE == type_select)
size_select = make_selection('These are the sizes: ', 'Which size do you need? Enter the number: ', size_subset)
length_subset = make_subset(table_new.LENGTH, (table_new.TYPE == type_select) & (table_new.SIZE == size_select))
length_select = make_selection('These are the available lengths: ', 'Which length do you need? Enter the number: ', length_subset)
vent_subset = make_subset(table_new.VENTED, (table_new.TYPE == type_select) & (table_new.SIZE == size_select) & (table_new.LENGTH == length_select))
vent_select = make_selection('These are the available lengths: ', 'Which length do you need? Enter the number: ', vent_subset)
part_number = make_subset(table_new['PART NUMBER'], (table_new.TYPE == type_select) & (table_new.SIZE == size_select) & (table_new.LENGTH == length_select) & (table_new.VENTED == vent_select))
print(part_number[1])
