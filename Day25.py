# Operations on tuples

countries = ("India", "Pakistan", "Afganistan", "Russia", "Nepal", "Bhutan")
countries2 = ("Australia", "America", "Korea", "Poland", "Germany")
tup = (1, 3, 4, 2, 4, 4, 5, 6, 7, 8, 2, 4, 5, 6, 6)
all_countries = countries + countries2
print("All Countries are:", all_countries)

print(countries[3].count("s"))
print(countries.index("Russia"))
print(tup.count(6))
print(tup.index(2))
print(tup.index(2, 4, 9)) # index(element, start, end)

# This state ment throws error since 10 is not present in the tuple
# print(tup.index(10))

# We directly can't change the tuple but we can manipulate it in a indirect way by changing the tuple to a list explicitly and then making changes and then changing it to tuple 
# Basically we can perform anything to the tuple by changing it into list but can not make changes in it directly

print(countries) # Before Changes

temp = list(countries) # changed tuple into list

# Here, we can do whatever changes we want in the tuple
temp.append("Bangladesh")
temp.pop("Pakistan")
temp[2] = "Japan"

countries = tuple(temp) # Changed list into tuple

print(countries) # After Changes