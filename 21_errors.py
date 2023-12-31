# print(0/0)

# print(result)
print('Hola')


def suma(a, b): return a + b


assert suma(1, 2) == 3

print('Hola 2')

age = 10
if age < 18:
    raise Exception('No puede ingresar')
