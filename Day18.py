# while loop
# while loop is used when we want the loop to be iterated while the condition is true

i = 0
while i <= 20:
    print(i, end = " ")
    i += 1

print("")

j = int(input("Enter a number: "))
while j <= 100:
    j = int(input("Enter a number: "))


# emulation of the do while loop in python
password = "python"
tries = 0

while True:
    word = input("Enter the password: ").lower()
    tries += 1

    if word == password:
        print("____You are Welcome Sir____")
        break
    if word != password and tries > 4:
        print("!! You are not trusted !!")
        break


# do while loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true but it will break at the moment it becomes false

num = 0

while True:
    num += 1
    if num <= 100:
        print(num)
        continue
    
    break