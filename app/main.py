import utils


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


def run():
    keys, values = utils.get_population()
    print(keys)
    print(values)

    country = input('Ingrese el pais: ')

    result = utils.population_by_country(data, country)
    print(result)


if __name__ == '__main__':
    run()
