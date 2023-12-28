numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_v2 = []

numbers_3 = map(lambda number: number * 2, numbers)

for number in numbers:
    numbers_v2.append(number * 2)

print(numbers_v2)
print(list(numbers_3))

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

result = map(lambda x, y: x + y, numbers_1, numbers_2)
print(list(result))
