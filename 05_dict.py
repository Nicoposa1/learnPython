'''''
dict = {}
for i in range(1, 5):
    dict[i] = i * 2
print(dict)

dict_v2 = {i: i * 2 for i in range(1, 5)}
print(dict_v2)

import random
countries = ["COL", "MEX", "BOL"]
population = {}
for country in countries:
    population[country] = random.randint(0, 100)
print(population)

population_v2 = {country: random.randint(0, 100) for country in countries}
print(population_v2)

'''
names = ["Juan", "Pedro", "Maria"]
ages = [18, 20, 22]
dict = {}
for i in range(len(names)):
    dict[names[i]] = ages[i]
print(dict)
print(list(zip(names, ages)))
dict_v2 = {names[i]: ages[i] for i in range(len(names))}
print(dict_v2)
dict_v3 = {name: age for name, age in zip(names, ages)}
print(dict_v3)