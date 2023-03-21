# If-else statements
# Conditional Operators 
# >, <, <=, >=, !=, ==

# print(a == 18)
# print(a >= 18)
# print(a <= 18)
# print(a < 18)
# print(a > 18)
# print(a != 18)

a = int(input("Enter your Age: "))
num = int(input("Enter a number: "))

# If
if a > 14:
    print("You can open a gmail account")

# If-else
if a >= 18:
    print("You can Drive")
else:
    print("You can't Drive")

# If-elif-else
if a < 5:
    print("Don't make jokes")
    print("I am not a toy you are playing with")
elif a < 18:
    print("You are not an adult")
else:
    print("You are a adult")

# Nested If-elif-else
if num < 0:
    print("This is a negative number")
elif num > 0:
    print("This is a positive number")
    if num > 0 and num < 20:
        print("Number is between 1-20")
        if num > 0 and num < 10:
            print("Number is between 1-10")
        else:
            print("Number is between 10-20")
    elif num > 20 and num < 40:
        print("Number is between 20-40")
        if num > 0 and num < 10:
            print("Number is between 20-30")
        else:
            print("Number is between 30-40")
    else:
        print("Number is greater than 40")
else:
    print("Number is a Zero")