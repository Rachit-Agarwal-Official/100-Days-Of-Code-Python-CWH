# Introduction to tuples
# Tuples are the immutable lists that can store multiple entities at a single location 

tup = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tup)
print(type(tup))
print("Length =", len(tup))
print("")
print(tup[1:])
print(tup[:8])
print(tup[-8:-2])
print(tup[0:7:2])

tup2 = tup[2:8]
print(tup2)

if 7 in tup:
    print("7 is present in the tuple")
else:
    print("7 is not present")

for i in tup:
    print(tup[i], end = "  ")