import random
countries = ["COL", "MEX", "BOL"]
population = {country: random.randint(1, 100) for country in countries}
print(population)

result = {country: population for (
    country, population) in population.items() if population > 40}
print(result)

text = 'Hola Soy Nicolas'
unique = {letter: letter.upper() for letter in text if letter in 'aeiou'}
print(unique)
