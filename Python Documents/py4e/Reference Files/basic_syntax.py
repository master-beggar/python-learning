import sys, os, random, numpy as np, webbrowser

count = 0
while count < 10:
    print(count)
    count = count + 1
print("Blast Off")

for i in range(5):
    print(i)

list1 = [1,2,3,4,5,67,8,8]
sortedlist = sorted(list1)
print(sortedlist)


list2=[]
for i in sortedlist:
    list2.append(i)
print(list2)

list2[2] = "hello"
print(list2)

np_list1 = np.array(list1)
print(np.mean(np_list1))

with open("names.txt", "r") as names:
    allnames = names.readlines()

for lines in allnames:
    for letters in lines:
        print(letters)

yourname = input("What is your name? ")


if yourname.lower() == "walid":
    print("you are the best")
