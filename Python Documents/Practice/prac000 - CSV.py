import csv
import numpy as np
import scipy.stats

date = []
close = []
volume = []

with open("nasdaq.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
        date.append(row[0])
        close.append(row[4])
        volume.append(row[6])
print(date)


exit()

dates = np.array(date[1:], dtype = "datetime64")
np_close = np.array(close[1:], dtype = "float")
np_volume = np.array(volume[1:], dtype = "float")

new_data = np.column_stack([np_close,np_volume])
print(new_data)
print(dates[7]-dates[0])

print("The correlatoin coefficient is :", np.corrcoef(np_close, np_volume))

ttest = scipy.stats.ttest_ind(np_close,np_volume,equal_var=False)
print(ttest)
# my_data = np.genfromtxt('nasdaq.csv', delimiter=',') straight to numpy array


# with open("new_dates", "w") as new_file:
#     writer = csv.writer(new_file, delimiter = "\t")
#     for row in reader:
#         writer.writerow(row)
