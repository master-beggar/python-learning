import math, os


# os.chdir("C:\Users\Ahmad Walid Naimi\Desktop\")

os.chdir(r"C:\Users\Ahmad Walid Naimi\Desktop")
print(os.getcwd())

family = [["mother", "45"], ["sister1", "27"], ["sister2","26"], ["brother", "25"]]

family2 = []
family1= []

for i in family:
    for j in i:
        family1.append(j)

#sorted function sorts from largest to smallest
print(sorted(family2))
print(family1.index("sister2")) #gives me the index of the list
print(family.count("sister1"))
family.reverse()
print(family)

dist = math.radians(23)*32
print("The distance is:", str(round(dist,2))+"mm")

with open("testing.txt","w") as testing:
    testing.write("Hello")
