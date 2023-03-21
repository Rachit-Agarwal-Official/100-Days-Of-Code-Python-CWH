# break and continue

# Continue is used to skip the iteration 
# Break is used to get out of the loop

for i in range(100):
    if i == 11:
        print("This is Nimit's age")
        continue
    if i == 14:
        print("This is my age")
        continue
    if i == 51:
        print("I am tired so I am breaking the loop")
        break
    print(i)