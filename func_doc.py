def printmax(x, y):
    '''Выводит максимальное из двух чисел.

    Оба обозначения должны быть целыми числами.'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')

printmax(3, 5)
print(printmax.__doc__)