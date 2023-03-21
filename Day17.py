# for loop
# for loop is used to iterate over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# To print every character of a string
name = "Rachit"
for i in name:
    print(i, end = " ")

print("")


# To print every value of the list
colors = ["Red", "Blue", "Green", "Yellow", "Black"]
for color in colors:
    print(color, end = " ")

print("")


# To print a range of numbers from zero to the number given
for j in range(5): # python automatically puts a zero as initial 'range(0, 5)'
    print(j, end = "  ")

print("")


# To print a range
for k in range(10, 20): # includes 10 and excludes 20
    print(k, end = "  ")

print("")


# To print a range with steps
for l in range(100, 200, 10): # includes 100 and excludes 200
    print(l, end = "  ")

# Reverse of the range with steps
for m in range(100, 1, -10):
    print(m, end = "  ")