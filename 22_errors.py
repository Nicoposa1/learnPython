
try:
    print(0/0)
    assert 1 != 1, 'No son iguales'
    age = 10
    if age < 18:
        raise Exception('No puede ingresar')
except ZeroDivisionError as error:
    print('Error')
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('Hola 2')
