empty_set = set()
numbers = {1,2,3,4,5,6,7,8}
l = ['bob', 'mike', 'bob', 'bob', 'drogon']

#sets don't have indexes like dictionaries
#making a list into a set will return a set with only unique values
list_to_set = set(l)
print('List to set:',list_to_set)

# to add an item to a set, use the .add method
empty_set.add(6)
# to add multiple items to a set, use the .update method
empty_set.update([7,8,9,10,11,12,13],[16])

print('This is the numbers set: ', numbers)
print('This is the empty set: ', empty_set)

# to view all items in both sets, also called union
all = numbers | empty_set
print('Union:', all)

# to view only items in common, also called intersection
common = numbers & empty_set
print('Common:',common)

# to view symmetric difference (items not in common)
not_common = numbers ^ empty_set
print('Not Common:', not_common)

# to view difference between sets
diff = numbers - empty_set
diff2 = empty_set - numbers
print('Diff: ', diff)
print('Diff2: ', diff2)
