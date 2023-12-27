def increment(x):
    return x + 1


def increment_v2(x): return x + 1


result = increment(2)
print(result)

result_v2 = increment_v2(2)
print(result_v2)


def full_name(first, last): return f'Full name is {first} {last}'

print(full_name('Nicolas', 'Posa'))