sum_total = 0
num_total = 0

while True:
    sval = input('Input a number: ')
    if sval == 'done':
        break
    else:
        try:
            fval = float(sval)
            num_total = num_total + 1
            sum_total = sum_total + fval
        except:
            print('Invalid Input')
            continue
print('the total number of items is', num_total, 'and the total sum is', sum_total)
