# Variables are memory locations that contains some kind of value
# There are 4 main Datatypes in python which are int, float, str, bool
# Other datatypes are complex, list, tuple, dictionary

a = "Rachit"
b = 14
c = True
d = 100.00
e = complex(14, 2)

print("")
print("Type of a is", type(a))
print("Type of b is", type(b))
print("Type of c is", type(c))
print("Type of d is", type(d))
print("Type of e is", type(e), "\n")

# List, Lists are mutable
list1 = ["Rachit", 14, True, 100.00]
print(type(list1))
print(list1)
print("")

# Tuple, Tuple are immutable
tuple1 = ("Rachit", 14, True, 100.00)
print(type(tuple1))
print(tuple1)
print("")

# Dictionary, Dictionary are key:value pairs, This is a mapped data
dict1 = {"name":"Rachit", "age":14, "class":10, "passion":"Coding"}
print(type(dict1))
print(dict1)
print("")