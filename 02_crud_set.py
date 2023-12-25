set_countries = {"USA", "China", "Japan"}

size = len(set_countries)
print(size)

print("USA" in set_countries)
print("Germany" in set_countries)

# Add an element to the set

set_countries.add("Germany")
print(set_countries)

# Update the set with another set
set_countries.update({"Argentina", "France"})
print(set_countries)

# Remove an element from the set
set_countries.remove("USA")
print(set_countries)

# set_countries.remove("USA")
set_countries.discard("US")
print(set_countries)

# Clear the set
set_countries.clear()
length = len(set_countries)
print(length)
