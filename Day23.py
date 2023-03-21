# List Methods

# This is a list l
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# append is used to add one more entity to the list at the last of the list
l.append(5)
print(l)

# pop is used to remove a entity from the list based on its index
l.pop(15)
print(l)

# sort is used to sort the list in ascending order
l.sort()
print(l)

# reverse = True argument in sort is used to sort the list in descending order
l.sort(reverse = True)
print(l)

# reverse is used to reverse the list
l.reverse()
print(l)

# index is used to find the index of a particular entity in the list
print(l.index(11))

# count is used to get the appearances of a particular entity in the list
print(l.count(1))

# copy is used to make a copy of the list instad of giving the referance
m = l.copy()
m[0] = 0
print(l)

# insert is used to insert a particular entity at a particular index
l.insert(1, "Added")
print(l)

# entend is used when we want to add the whole content of the other list to the list 
n = [1000, 1100, 1200]
l.extend(n)
print(l)

# This is a method to concatinate two strings together and store them in a new one
k = l + n
print(k)