def get_population(country_dict):
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def get_world_percentage(data):
    # {'Rank': '36', 'CCA3': 'AFG', 'Country/Territory': 'Afghanistan', 'Capital': 'Kabul', 'Continent': 'Asia', '2022 Population': '41128771', '2020 Population': '38972230', '2015 Population': '33753499', '2010 Population': '28189672', '2000 Population': '19542982', '1990 Population': '10694796', '1980 Population': '12486631', '1970 Population': '10752971', 'Area (km²)': '652230', 'Density (per km²)': '63.0587', 'Growth Rate': '1.0257', 'World Population Percentage': '0.52'}
    total_population = 0
    for country in data:
        total_population += int(country['2022 Population'])
    for country in data:
        percentage = round(
            (int(country['2022 Population']) / total_population) * 100, 2)
        country['World Population Percentage'] = percentage
    return data


def population_by_country(data, country):
    result = list(
        filter(lambda item: item['Country/Territory'] == country, data))
    return result
