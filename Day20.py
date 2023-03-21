# Functions
# Functions are used when we want to separate the logic of a certain function/proess to use it whenever we want without writing the logic again

def swap(a, b):
    temp = a
    print("Before Swapping:", "a =", a, "| b =", b)
    a = b
    b = temp
    print("After Swapping:", "a =", a, "| b =", b)

def reverse():
    pass # This is used when we want to write the function body later 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
swap(a, b) # This is the function call