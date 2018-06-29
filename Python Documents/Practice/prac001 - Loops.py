import csv

for i in range(10):
    print(i+1)

x = 0
while x < 10:
    print(x)
    x += 1a

with open("nasdaq.csv") as nasdaq:
    naslist = csv.DictReader(nasdaq)
    writer = []
    numbers =[]
    for row in naslist:
        writer.append(row["Open"])
    for number in writer:
        numbers.append(int(number))

x = "234"
x = int(x)
print(type(x))

# def addition(numbers):
