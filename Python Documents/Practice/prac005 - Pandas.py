import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st

filename = r'C:\Users\Ahmad Walid Naimi\Desktop\airquality.csv'
data = pd.read_csv(filename)

print(data)
exit()
print(data.dtypes) #'object' type in pandas means that its a string
print(data[data.Ozone.isnull()])
data.Close = pd.to_numeric(data.Close)
print(data.index)

# data.dropna() will drop all the rows with an NaN but change the index
# data.drapna(inplace = True) will drop NaN but keep the indices as is

data.Close = data.Close.astype(int)
print(data.dtypes)

data.Date = pd.to_datetime(data.Date)

plt.plot(data.Close)
plt.show()
