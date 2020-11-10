def my_func(x: float, y: int):
    res = 1
    for i in range(abs(y)):
        res *= x
    return x ** y, 1 / res


print(my_func(1.5, -2))
