import matplotlib.pyplot as plt


def generete_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def generete_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    values = [1, 4, 2, 5, 3]
    # generete_bar_chart(labels, values)
    generete_pie_chart(labels, values)
