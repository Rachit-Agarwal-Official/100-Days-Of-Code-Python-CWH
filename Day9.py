# TypeCasting

# Implicit Typecasting
a = 10
b = 10.0
c = a + b # Here python changed "a" into a float value
print(c)

print("Type of a is:", type(a))
print("Type of b is:", type(b))
print("Type of c is:", type(c))

# Explicit Typecasting

x = "1"
y = "2"
print(x + y) # String Concatination
print(int(x) + int(y)) # Explicitly typecasted a string into a integer