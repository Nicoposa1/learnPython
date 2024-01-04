import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./app/data.csv')
    print(data[0])
    data = list(
        filter(lambda item: item['Continent'] == 'South America', data))

    country = list(map(lambda x: x['Country/Territory'], data))
    percentage = list(map(lambda x: x['World Population Percentage'], data))
    charts.generete_pie_chart(country, percentage)

    # country = input('Ingrese el pais: ')
    # result = utils.population_by_country(data, country)

    # if len(result) > 0:
    #     country = result[0]
    #     labels, values = utils.get_population(country)
    #     charts.generete_bar_chart(labels, values)

    # result = utils.get_world_percentage(data)
    # if len(result) > 0:
    #     labels = []
    #     values = []
    #     for country in result[:10]:
    #         labels.append(country['Country/Territory'])
    #         values.append(country['World Population Percentage'])
    #     charts.generete_pie_chart(labels, values)



if __name__ == '__main__':
    run()
