price = 100 # Global variable


def increment():
    price = 200
    result = price + 10
    print(result)
    return result

result = increment()
print(result)
