def my_func(a, b, c):
    digits = [a, b, c]
    max_elem = max(digits)
    digits.remove(max_elem)
    return max_elem + max(digits)


print(my_func(1, 2, 3))
