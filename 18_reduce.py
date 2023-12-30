import functools
numbers = [1, 2, 3, 4, 5]


def acum(counter, item):
    results = counter + item
    return results


result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

acum_result = print(acum(1, 2))
