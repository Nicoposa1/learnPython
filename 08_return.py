sum = 0
for i in range(1, 10):
    sum += i

print(sum)


def sum_with_range(a, b):
    sum = 0
    for i in range(a, b):
        sum += i
    return sum


result = sum_with_range(1, 34)
print(result)
