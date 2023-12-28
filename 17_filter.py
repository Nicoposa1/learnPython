numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_v2 = list(filter(lambda number: number % 2 != 0, numbers))

print(numbers_v2)
