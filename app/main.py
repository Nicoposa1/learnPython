import utils
keys, values = utils.get_population()
print(keys)
print(values)

data = [
    {
        "Country": "arg",
        "Population": 300
    },
    {
        "Country": "uru",
        "Population": 400
    }
]

country = input('Ingrese el pais: ')

result = utils.population_by_country(data, country)
print(result)
