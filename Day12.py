# String Slicing
# name[starting index : ending index : gaps/spaces]

name = "Rachit"
print(name[0:6]) # Including the 0th and excluding the 6th index
print(name[1:5])
print(name[:6]) # Automatically it puts a 0
print(name[0:]) # Automatically it puts the length of the string
print(name[:])
print(name[0:-2])
print(name[-3:-1]) # In negative indexing print(name[len(name)-3:len(name)-1])
print(name[0:6:2])
print(name[len(name)::-1])