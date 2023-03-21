# Function Arguments
# We can define the arguments in function definition in various ways 

# Putting them as required
def average1(a, b):
    ans = (a + b)/2
    print(ans)

average1(5, 5)


# Initializing them so that it will be optional
def average2(a = 4, b = 4):
    ans = (a + b)/2
    print(ans)

average2(5, 5)
average2(a = 5, b = 5)
average2(b = 6)


# Put them as a tuple
def average3(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(sum/len(numbers))

average3(5, 5)


# Put them as a dictionary
def name(**names):
    print("Hello,", names["fname"], names["mname"], names["lname"])

name(fname = "Rachit", mname = "Agarwal", lname = "Sir")