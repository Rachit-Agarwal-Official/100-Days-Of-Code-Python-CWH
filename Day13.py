# Strings are immutable 
# Whenever we are performing any method we are actually doing it with a copy of the string

a = "Rachit"
b = "!!!Rachit!!!"
c = "Rachit Is A Good Boy 1234"
d = "rachit iS a coDeR"
e = "Rachit is a good boy, Rachit is a Coder"
f = "RachitIsAGoodBoy1234\n"

print("String a in uppercase is:", a.upper())
print("String a in lowercase is:", a.lower())
print("String b with ! on both side stripped is:", b.strip("!"))
print("String b with ! on trailing side stripped is", b.rstrip("!"))
print("String c with Rachit replaced with Nimit is:", c.replace("rachit", "Nimit"))
print("String c with blank spaces splitted is:", c.split(" "))
print("String d capitalized is:", d.capitalize()) 
print("String c centered on 30 characters is:" + c.center(30))
print("Number of times 'Rachit' occured in String e is:", e.count("Rachit"))
print("Is string c ending with '!' ?:", c.endswith("!"))
print("Is string b starting with '!' ?:", b.startswith("!"))
print("Index of first occurance of 'i' in String c is:", c.find("i"))
print("Is Alphanumeric:", f.isalnum())
print("Is Alpha:", f.isalpha())
print("Is Lower:", c.islower())
print("Is Lower:", c.isupper())
print("Is Printable:", f.isprintable())
print("Is string only space:", c.isspace())
print("Is Title:", c.istitle())
print("Swap the cases of string c:", c.swapcase())
print("Make string d a title: ", d.title())
print("Throw error if 'Rahul' is not found in String c", c.index("i"))