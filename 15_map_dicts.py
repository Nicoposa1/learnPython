items = [
    {
        "id": 1,
        "name": "laptop",
        "price": 100,
    },
    {
        "id": 2,
        "name": "mouse",
        "price": 40,
    },
    {
        "id": 3,
        "name": "monitor",
        "price": 400,
    },
]

prices = list(map(lambda item: item['name'], items))
print(prices)


def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item


new_items = list(map(add_taxes, items))
print(new_items)
