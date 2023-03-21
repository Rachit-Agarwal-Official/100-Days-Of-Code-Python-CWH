# Introduction to Lists
languages = ["Python", "Java", "C", "C++", "JavaScript", "Kotlin"]
print(languages)
print("Length =", len(languages))
print(type(languages))
print(languages[:]) # Automatically fills langauges[0:len(languages)]
print(languages[:-5])
print(languages[-6:-1]) # Negative Indexing
print(languages[len(languages)-6:len(languages)-1]) # Positive Indexing
print(languages[6-6:6-1]) # Positive Indexing
print(languages[0:5]) # Positive Indexing
print(languages[0:6:2]) # Jump Indexing
print(languages[::-1]) # Reversing the list
print(languages[::-2]) # Reversing the list with 2 jumps


# To check if a entity is in the list or not
devices = ["Laptop", "Mouse", "Printer", "Headphones", "Keyboard"]

if "Monitor" in devices:
    print("You have a monitor")
else:
    print("No problem you'll get a monitor soon")

if "Laptop" in devices:
    print("You have a Laptop")
else:
    print("No problem you'll get a laptop soon")


# List Comprehension
# Syntax:-  variable = [expression for item in iterable condition]

names = ["Rachit", "Rohan", "Rocky", "Rancho", "Nimit"]
lst = [item for item in names if "o" in item]
print(lst)